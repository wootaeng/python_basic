# 조건문
# : 조건에 따라 실행할 명령이 달라 지는 것

origin_pass = "1234" 
input_pass = input("패스워드를 입력하세요 >>>")

if origin_pass == input_pass: # 조건 A
    # 조건 A 참
    print("비밀번호가 맞습니다.")
elif input_pass == "": # 조건 B
    # 조건 A 거짓, 조건 B 참
    print("아무것도 입력하지 않았습니다.")
else: 
    # 조건 A, 조건 B 거짓
    print("비밀번호가 틀립니다.")