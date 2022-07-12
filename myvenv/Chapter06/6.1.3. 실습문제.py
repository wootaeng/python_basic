# 로또 예상번호 추출 프로그램
# 1. 로또 번호 6개를 생성
# 2. 로또 번호는 1-45 까지 랜덤
# 3. 6개의 숫자 모두 달라야함
# 4. getRandomNumber() 함수를 사용해서 구현

import random

def getRandomNuber():
    number = random.randint(1,45)    
    
    return number

lotto_num = [] # 로또 번호를 저장할 리스트

# for i in range(6): # 반복 가능, 중복 값도 발생
#     random_number = getRandomNuber()
#     lotto_num.append(random_number)

# 중복값 없이 작동 프로그램

count = 0 # 현재 뽑은 숫자 개수

while True:
    if count > 5:
        break
    random_number = getRandomNuber()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1
        
    
    
lotto_num.sort()
# print(lotto_num)

for num in lotto_num:
    print(num, end = " ")

