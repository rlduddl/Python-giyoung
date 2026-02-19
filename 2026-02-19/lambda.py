
# 파일을 엽니다
file = open("basic.txt", "w")

# 파일에 텍스트를 씁니다.
file.write("Hello Python Promgramming...!")

# 파일을 닫습니다.
file.close()


# with 키워드
with open("basic.txt", "w", encoding="utf-8") as file:
    file.write("hi")





import random

hanguls = list("가나다라마바사아차카타파하")

with open("info.txt", "w", encoding="utf-8") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 188)
        height = random.randrange(140,200)

        file.write("{},{},{}\n".format(name, weight, height))

# 파일 처리

with open("info.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        # 1️⃣ 빈 줄 제거
        if not line:
            continue

        # 2️⃣ 쉼표 기준 분리 (공백 유무 상관없이 처리)
        parts = line.split(",")

        # 3️⃣ 데이터 개수 검증
        if len(parts) != 3:
            continue

        # 4️⃣ 공백 제거
        name, weight, height = [p.strip() for p in parts]

        try:
            weight = float(weight)
            height = float(height)

            # 5️⃣ BMI 계산
            bmi = weight / ((height / 100) ** 2)

        except ValueError:
            # 숫자 변환 실패 시 스킵
            continue

        # 6️⃣ 판정
        if bmi >= 25:
            result = "과체중"
        elif bmi >= 18.5:
            result = "정상 체중"
        else:
            result = "저체중"

        # 7️⃣ 출력
        print(f"""
이름: {name}
몸무게: {weight}
키: {height}
BMI: {bmi:.2f}
결과: {result}
""")