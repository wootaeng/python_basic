# 턱걸이 횟수를 빈 리스트에 저장하고 
# 해당값들의 평균을 구하라

data = [] # 빈 리스트

x = int(input("1일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("2일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("3일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("4일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("5일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("6일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("7일차 턱걸이 횟수 >>>"))
data.append(x)

total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]
avg = total/7

print(int(avg))
