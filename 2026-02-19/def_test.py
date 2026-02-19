def print_3_times():
    print("안녕")
    print("안녕")
    print("안녕")
    print()
print_3_times()

def print_n_times(value, n):
    for i in range(n):
        print(value)


print_n_times("안녕하세요", 5)


# 가변 매개변수

def print_n_times2(n, *values):
    # n번 반복합니다.
    for i in range(n):
        # values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        
        # 단순한 줄바꿈
        print()
    

# 함수를 호출
print_n_times2(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")


# 기본 매개변수

def print_n_ntimeS(value, n=2):
    # n번 반복합니다.
    for i in range(n):
        print(value)

    
#  함수를 호출합니다
print_n_ntimeS("하이요")