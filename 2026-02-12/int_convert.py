String_a = input("입력A> ")
int_a= int(String_a)

String_b = input("입력B> ")
int_b = int(String_b)

print("문자열 자료:", String_a + String_b)
print("숫자 자료:", int_a + int_b)



str_input = input("숫자 입력> ")
num_input = float(str_input)
print()
print(str(num_input)+"inch")
print(str(num_input * 2.54)+"cm")




str_input2 = input("원의 반지름 입력>")
num_input2 = float(str_input2)
print()
print("반지름: ", num_input2)
print("둘레: ", 2*3.14*num_input2)
print("넓이: ", 3.14*num_input2**2)


num_input2 = float(input("원의 반지름 입력>"))


# ----------변수 스왑---------
a = input("문자열 입력> ")
b = input("문자열 입력>")

print(a, b)

c = a
a = b
b = c


print(a, b)

