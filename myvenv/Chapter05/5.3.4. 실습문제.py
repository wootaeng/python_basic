# Learning korean

# 한국어 리스트
word_list = ["당첨", "성공", "이로치", "백백"]

# 점수
score = 0

print("Let's Learning Korean")

for word in word_list:
    print(word)
    data = input()
    if data == word:
        score += 1
        
print("전체 문제 개수 : ", len(word_list))
print("맞힌 개수 : ", score)
print("틀린 개수 :", len(word_list)-score)

# 전체 문제 개수 : 4개
# 맞힌 문제 개수 : 2개
# 틀린 문제 개수 : 2개