# - 변수
# 1. 데이터를 저장할 공간
# 2. 언제든지 데이터를 변경 할 수 있다

# 변수이름 = 데이터 ( = 할당연산자 )

# - 변수 이름 짓는 규칙
# 1. 데이터를 표현할 수 있는 이름으로 짓는다
# 2. 문자부터 시작해야 한다
# 3. 대소문자는 구분한다
# 4. _ 로 시작할 수 있다
# 5. 미리 예약된 키워드는 사용할 수 없다

# 마스터이 챔피언 데이터를 변수에 저장



name = "마스터이"
level = 5
health = 800
attack = 90
print(name, level, health, attack)

# 변수에 저장된 데이터를 변경하기
# level = 6
# health = 900
# attack = 105
level = level + 1
health = health + 100
attack = attack + 15
print(name, level, health, attack)