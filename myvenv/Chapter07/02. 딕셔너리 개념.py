# 딕셔너리
# : 사전형태의 자료형

# 딕셔너리 만들기
stock_a = {"삼성전자" : 58000, "LG전자" : 150000}

stock_b = {
    "삼성전자" : [81000,1230000,324000, 4214090], #리스트형
    "LG전자" : (12000,1250000,245345,1234125) #튜플형
}

stock_c = {
    "삼성전자" : { #중복형태 딕셔너리 안 딕셔너리
        "현재가" : 8200,
        "보유수량" : 5,
        "매수단가" : 81000
    }
}


# print(stock_a)
# print(stock_b)
# print(stock_c)

# 딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기
stock_a["삼성전자"] = 85000
print(stock_a)

# 딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)

# 딕셔너리 함수
stock_d = {
    "삼성전자" : 8200,
    "SK 하이닉스" : 123000,
    "NAVER" : 370000,
    "카카오" : 133000
}
# items() : 키와 데이터 쌍
print(stock_d.items())

for item in stock_d.items():
    print(item) # 튜플식
    # print(item[0]) # 데이터만
    # print(item[1]) # 키값만 
    
# keys() : 키
for key in stock_d.keys():
    print(key)
    
# values() : 데이터
for value in stock_d.values():
    print(value)
