# 숫자1 입력 : "게임을 시작합니다"
# 숫자2 입력 : "실시간 랭캉"
# 숫자3 입력 : "게임을 종료합니다" 후 프로그램 종료
# 3 입력 전에는 계속 실행. 1-3 외에는 "다시입력해주세요"

while True:
    print("[메뉴를 입력하세요")
    x = int(input("1. 게임시작 2. 랭킹보기 3.게임종료 >>>"))
    if x == 1:
        print("게임을 시작합니다")
    elif x == 2:
        print("실시간 랭킹")
    elif x == 3:
        print("게임을 종료합니다")
        break
    else:
        print("다시 입력해주세요")