# 튜플의 특징
# : 읽기 전용 리스트
# 시퀀스 자료형
# 수정, 추가, 삭제가 불가능한 리스트
# 메모리 사용이 효율적
# 읽기만 가능하기 때문에 데이터 손실 염려가 없다

a = (3,4,5)
b = 3,4,5

c = (3,)
d = 3,

e = tuple([3,4,5])
f = list(range(10))
g = tuple(f)

h = 3,4,5
i = list(h)

# 패킹 
# : 여러개의 데이ㅓ를 하나의 변수에 할당하는 것

# 언패킹
# : 컬렉션의 각 데이터를 각각의 변수에 할당하는 것

x = 10,20,30,40,30

x.index(20) #특정값의 인덱스 구하기. 20의 순서. 1
x.count(30) #특정값의 개수. 30의 개수. 2
max(x), min(x) #최대값 40, 최소값 10
sum(x) #값들의 합 130