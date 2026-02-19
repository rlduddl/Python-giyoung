import requests
import time
from datetime import datetime, timedelta
# 기상청 API 기본 정보
URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
SERVICE_KEY = "m/9ulN8H26aqVrla7rEWNsWkwHUeETYZ4CfmqTdGYFSu07y3XVxIAMVDxIB7kxMyLJ9OMCn1Aj4UtU7Mz2vBrg=="
# 전국 주요 도시 좌표
CITIES = {
    "서울": (60, 127),
    "부산": (98, 76),
    "대전": (67, 100),
    "광주": (58, 74),
    "인천": (55, 124),
    "대구": (89, 90),
    "울산": (102, 84),
    "제주": (52, 38),
    "강릉": (92, 131),
    "춘천": (73, 134)
}
# 기상청 발표 시간
TIMES = ["0200", "0500", "0800", "1100", "1400", "1700", "2000", "2300"]

def get_base_times():
    """현재 시간 기준으로 가능한 base_time 리스트 반환 (fallback 포함)"""
    now = datetime.now()
    current_time = now.strftime("%H%M")
    today = now.strftime("%Y%m%d")
    yesterday = (now - timedelta(days=1)).strftime("%Y%m%d")
    base_times = []
    for t in reversed(TIMES):
        if current_time >= t:
            base_times.append((today, t))
    if not base_times:
        base_times.append((yesterday, "2300"))
    if len(base_times) < len(TIMES):
        for t in reversed(TIMES):
            base_times.append((yesterday, t))
    return base_times

def request_weather_data(params):
    """API 요청 (재시도 로직 포함)"""
    for attempt in range(2):
        try:
            res = requests.get(URL, params=params, timeout=10)
            return res.json()
        except Exception as e:
            print(f"⚠️ API 호출 실패 (재시도 {attempt+1}) : {e}")
            time.sleep(1)
    return None

def get_weather(nx, ny):
    """특정 좌표의 날씨 조회"""
    base_times = get_base_times()
    for base_date, base_time in base_times:
        params = {
            "serviceKey": SERVICE_KEY,
            "numOfRows": "500",
            "pageNo": "1",
            "dataType": "JSON",
            "base_date": base_date,
            "base_time": base_time,
            "nx": nx,
            "ny": ny
        }
        data = request_weather_data(params)
        if not data:
            continue
        # NO_DATA 처리
        if data.get("response", {}).get("header", {}).get("resultCode") == "03":
            print(f"[{nx}, {ny}] {base_date} {base_time} NO_DATA → 이전 발표 시간으로 재시도")
            continue
        try:
            items = data["response"]["body"]["items"]["item"]
        except KeyError:
            print(f"[{nx}, {ny}] 응답 JSON 구조 오류: {data}")
            continue
        temp, wf = None, None
        for item in items:
            if item["category"] == "TMP" and temp is None:
                temp = item["fcstValue"]
            if item["category"] == "SKY" and wf is None:
                wf = {
                    "1": ("맑음", "☀️"),
                    "3": ("구름많음", "⛅"),
                    "4": ("흐림", "☁️")
                }.get(item["fcstValue"], ("데이터 없음", "❓"))
            if temp and wf:
                break
        if temp or wf:
            return {
                "temp": temp if temp else "-",
                "wf": wf[0] if wf else "데이터 없음",
                "icon": wf[1] if wf else "❓"
            }
    # 모든 발표 시간 실패 시
    return {"temp": "-", "wf": "데이터 없음", "icon": "❓"}

def get_all_cities_weather():
    """전국 주요 도시의 날씨를 한꺼번에 조회"""
    all_weather = []
    for city, (nx, ny) in CITIES.items():
        weather = get_weather(nx, ny)
        all_weather.append({
            "city": city,
            "wf": weather["wf"],
            "icon": weather["icon"],
            "temp": weather["temp"]
        })
    return all_weather