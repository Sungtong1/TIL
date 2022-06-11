pn = [0 for i in range(1050)]
for i in range(2, 32):
    for j in range(i * 2, 1050, i):
        pn[j] = 1
n = input()
word = 0
for i in n:
    if i.islower() == True:
        word += ord(i) - 96
    else:
        word += ord(i) - 38
if pn[word] == 0:
    print('It is a prime word.')
else:
    print('It is not a prime word.')