# 회사를 그만두게 된 유진이는 유투브를 시작
# 프로그램 사용자로부터 현재 구독자 수 입력 받으면, 수익창출 여부 프로그램 작성
# 수익창출은 구독자가 1000명 이상이어야 가능

viewer = int(input("현재 구독자 수를 입력하세요 >>>"))

if viewer >= 1000 :
    print("수익 창출이 가능합니다!")
elif viewer < 1000 :
    print("수익 창출이 불가능합니다.")
