# 팔굽혀펴기 개수이다 데이터는 리스트에 저장 되어 있다. 
# 각 문항을 실행한 결과를 출력해 보자


result = [33,40,12,63,52]
print(result)

# 문항 1 
# 6번의 팔굽혀펴기 개수는 9개이다. 리스트의 마지막에 추가하자
result.append(9)
print(result)

# 문항 2
# 2번은 재측정하여 50개를 하였다. 2번의 데이터를 변경해보자
result[1] = 50
print(result)

# 문항 3
# 3번부터 6번까지 데이터를 슬라이싱하자
print(result[2:6])

# 문항 4
# 모든 데이터를 오름차순으로 정렬하자
result.sort()
print(result)