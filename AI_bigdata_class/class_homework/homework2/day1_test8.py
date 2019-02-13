#8

# 주어진 문자열에 문자 a 가 몇개 있는지 구하는 프로그램을 작성하시오. (for문 사용)

word = 'banana'

word_len = len(word)
word_lst = list(word)
print(word_len)
cnt = 0

for i in range(word_len):
    if word_lst[i] == 'a':
        cnt += 1

print("'a'의 개수는 %d개 입니다." %cnt)