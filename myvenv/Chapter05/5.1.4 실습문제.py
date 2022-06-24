# 국어, 수악, 영어 성적이 입력된다.
# 세 과목의 평균점수가 80점 이상이면 합격. 
# 그런데 오류 발생으로 80점 이상일 경우 불합격이 되도록 프로그램 작성
# (단, 0점 - 100점 사이의 숫자를 입력하지 않으면 "잘못입력" 출력)

ko = int(input("국어>>>"))
math = int(input("수학"))
en = int(input("영어>>>"))

avg = (ko + math + en)/3

# 방법 1

if ko>100 or ko < 0 or math > 100 or math < 0 or en > 100 or en < 0 :
    print("잘못 입력하였습니다")
    
elif avg < 80:
    print("합격")
else :
    print("불합격")
    
# 방법 2

if 0 <= ko <= 100 and 0 <= math <= 100 and 0 <= en <= 100:
    if avg >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다.")