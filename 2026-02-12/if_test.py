#날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()
print(now)



#오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

#오후 구분
if now.hour >= 12:
    print("현제 시각은 {}시로 오후입니다!".format(now.hour))    

# 봄 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

# 여름 구분
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

# 가을 구분
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

# 겨울 구분
if now.month == 12 or 1 <= now.month <= 2 :
    print("이번 달은 {}월로 겨울입니다!".format(now.month)) 



# 입력을 받습니다.
number = input("정수입력> ")

# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

# 짝수 확인
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다")

# 홀수 확인
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수입니다")


#짝수 조건
if last_character in "02468":
    print("짝수입니다")

#홀수 조건
if last_character in "13579":
    print("홀수입니다")


# 입력을 받습니다.
number = input("정수입력>")
number = int(number)

#짝수 조건
if number % 2 == 0 :
    print("짝수입니다")

#홀수 조건
if number % 2 == 1 :
    print("홀수입니다")






a = int(input("> 1번째숫자: "))
b = int(input("> 2번째 숫자:")) 

if a> b:
    print("처음 입력했던 {}가 {}보다 더 큽니다".format(a,b))


if b > a:
    print("두번째로 입력했던 {}가 {}보다 더 큽니다".format(b,a))





# 중첩 조건문
x = float(input("정수입력"))

if x > 10:
    if x < 20:
        print("조건에 맞습니다.")

else :
    print("조건불충족")


if x >10 and x<20 :
    print("조건충족")

else :
    print("조건불충족")

if 10<  x<20 :
    print("조건충족")

else :
    print("조건불충족")