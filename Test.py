print("Hello, World!")

age = 20
height = 175.5
print("나이:", age, "키:", height)

name = "Alice"
print("안녕하세요, " + name + "님!")
print(f"안녕하세요, {name}님!")  # f-string 사용

number = 10
if number > 5:
    print("5보다 큽니다.")
else:
    print("5보다 작거나 같습니다.")

for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

fruits = ["사과", "바나나", "딸기"]
for fruit in fruits:
    print(fruit)

def greet(name):
    return f"안녕하세요, {name}님!"

print(greet("Bob"))

name = input("이름을 입력하세요: ")
print(f"반갑습니다, {name}님!")

num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))
print("합계:", num1 + num2)
