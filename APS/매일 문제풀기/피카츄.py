# 백준 피카츄

word = input()
word_len = len(word)
idx = 0
result = 'YES'
usable_word = ['pi','ka','chu']

if word_len <= 1:
    result = 'NO'
else:
    while True:
        tmp = ''
        for i in range(3):
            if idx == word_len:
                result = "NO"
                break
            tmp += word[idx]
            idx += 1
            if tmp in usable_word:
                break
        else:
            result = "NO"
            break
        if idx == word_len:
            break
print(result)
