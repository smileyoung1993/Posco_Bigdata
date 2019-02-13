#5
'''
# while반복문

word = 'Python'

word_lst = list(word)

i = 0
word_len = len(word_lst)

while True:

    print(word_lst[i])

    i+=1

    if i == word_len:
        break
'''

# for문

word = 'Python'

word_lst = list(word)

for unit in word_lst:
    print(unit)