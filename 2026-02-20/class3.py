# 딕셔너리를 리턴하는 함수를 선언합니다.
def create_student (name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math": math,
        "english": english,
        "science": science
    }

# 학생을 처리하는 함수를 선언합니다.
def student_get_sum(student):
    return student["korean"] + student["math"] +\
        student["english"] +student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )

# 학생 리스트 선언합니다.
students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연인성", 97, 98, 18, 98),
    create_student("구인성", 24, 99, 28, 85),
    create_student("나인성", 55, 99, 28, 91),
    create_student("윤아린", 82, 28, 48, 25),
    create_student("윤명월", 89, 78, 88, 75)
]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    # 출력합니다
    print(student_to_string(student))
                