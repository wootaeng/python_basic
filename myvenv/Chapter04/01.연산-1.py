# 1. 대입연산
# 변수이름 = 데이터

# 2. 산술연산
# - 숫자연산


from os import access


x = 5
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y) # 몫
print(x%y) # 나머지
print(x**y) # 제곱


# - 문자열연산
tag1 = "#집에가지"
tag2 = "#집에안가냐"
tag3 = "#집좀가자"
 
 
tag = tag1 + tag2 + tag3
print(tag)

message = "파이썬 코틀린 언제 다하지.\n" *5 # \n을 넣으면 줄바꿈
print(message)

# 복합할당연산자
level = 10 # (레벨 1 증가)
level += 1    #level = level +1

health = 200 # (체력 300 감소)
health -= 300 #health = health - 300

attack = 300 # (공격력 1.5 배 증가)
attack *= 1.5 #attack = attack * 1.5

speed = 400 # (이동속도 50% 감소)
speed /= 2  #speed = speed /2


print(level, health, attack, speed)