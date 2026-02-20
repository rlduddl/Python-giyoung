# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )
    
 # 학생 리스트 선언합니다.
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연인성", 97, 98, 18, 98),
    Student("구인성", 24, 99, 28, 85),
    Student("나인성", 55, 99, 28, 91),
    Student("윤아린", 82, 28, 48, 25),
    Student("윤명월", 89, 78, 88, 75)
]
    
# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")

for student in students:
    # 출력합니다
    print(student.to_string())