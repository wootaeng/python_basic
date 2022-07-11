# Learning korean

# 한국어 리스트
word_list = ["당첨", "성공", "이로치", "백백"]

print("Let's Learning Korean")

for word in word_list:
    print(word)
    data = input()
    if data != word:
        print("다시 입력하세요")
        break
# 전체 문제 개수 : 4개
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개