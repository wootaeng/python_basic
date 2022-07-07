# 기본형
# 1. 정의하기
from random import random


def printHello():
    print("Hello")
    
# 2. 호출하기
printHello()

# 매겨변수가 있는 함수
def sum(a,b):
    print(a + b)
    
sum(1,3)

# 반환값이 있는 함수
def getRandomNumber():
    number = random.radint(1,10)
    return number