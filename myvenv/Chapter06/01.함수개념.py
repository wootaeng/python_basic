# 함수를 사용하는 이유
# 수정의 용이성
# 가독성
# 자동화?

# 함수를 사용하지 않은 경우
print("안녕하세요. 칠팔이님")
print("현재 메타그로스 백이 없습니다")

print("안녕하세요. 칠팔이님")
print("현재 메타그로스 98이 없습니다")

print("안녕하세요. 칠팔이님")
print("현재 메타그로스 95가 없습니다")

# 함수를 사용한 경우
def printMessage(name, date):
    print("안녕하세요",name,"님")
    print("현재 메타그로스 ", score, "이(가) 없습니다.")
    
printMessage("칠팔이",100)
printMessage("칠팔이",98)
printMessage("칠팔이",95)