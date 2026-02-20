class Person:
    def __init__(self, name, age):
        self.name = name   # 속성(attribute)
        self.age = age
    def introduce(self):   # 메서드(method)
        print(f"안녕하세요. 저는 {self.name}이고 {self.age}살입니다.")

# 객체 생성
p1 = Person("철수", 20)
p2 = Person("영희", 25)
# 메서드 호출
p1.introduce()
p2.introduce()


class Car:
    def __init__(self, model):
        self.model = model
    def drive(self):
        print(f"{self.model}이(가) 달립니다!")

car1 = Car("BMW")
car2 = Car("벤츠")
car1.drive()
car2.drive()


class Dog:
    species = "포유류"  # 클래스 속성 (모든 개가 공유)
    def __init__(self, name):
        self.name = name  # 인스턴스 속성

d1 = Dog("바둑이")
d2 = Dog("초코")
print(d1.name, d1.species)
print(d2.name, d2.species)



class MathTool:
    @classmethod
    def info(cls):
        print("이건 클래스 메서드입니다.")
    @staticmethod
    def add(a, b):
        return a + b
MathTool.info()
print(MathTool.add(3, 5))


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}원 입금! 현재 잔액: {self.balance}원")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount}원 출금! 현재 잔액: {self.balance}원")
        else:
            print("잔액 부족!")
acc = BankAccount("홍길동", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)




class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    def attack_enemy(self, enemy):
        enemy.hp -= self.attack
        print(f"{self.name}가 {enemy.name}을(를) 공격! 남은 체력: {enemy.hp}")

player = Character("용사", 100, 20)
monster = Character("고블린", 50, 10)
player.attack_enemy(monster)
monster.attack_enemy(player)