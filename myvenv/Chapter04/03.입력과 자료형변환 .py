# 정리
# 사용자로부터 입력받기
# 1. input("입력할 시 출력할 메세지")

# 2. 자료형 변환
# 숫자형으로 변환
# int(데이터)

# 실습문제 4.3.1
# 사용자로부터 두개의 숫자를 입력 받고,
# 더한 결과를 출력하기 
from unittest import result


x = input("첫번째 숫자를 입력하세요 >>>")
y = input("두번째 숫자를 입력하세요 >>>")

# result = x+y
# print(x+y)

# 자료형 확인하기 : type(x)
# 현재는 str = string 상태

# 숫자형으로 변환
# int 함수를 사용 : int(데이터)

result = int(x)+int(y)
print(result)


# 실습문제 4.3.2
# 사용자로부터 태어난 연도를 입력 받으면,
# 현재 나이를 출력하기

# current_year = 2022

# x = input("태어난 연도를 입력하세요 >>>")
# birth = int(x)

# age:int = current_year - birth

# print("현재나이는 " +str(age) +" 입니다.")

year = int(input("태어난 연도를 입력하세요 >>>"))
age = 2022 - year + 1
print("현재 나이는 ", str(age), "세 입니다.")