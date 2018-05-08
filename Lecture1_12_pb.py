import string
import random
import time

def stringNew(list0, N):
    str0 = ''
    for i in range(N):
        ichar = random.choice(list0)
        str0 += ichar
    str0 += ' '
    return str0

def strcmp(x, y):
    score0 = 0
    for i in range(len(x)):
        if x[i] == y[i]: score0 += 1
    return score0 / len(x)

chrlist = string.ascii_lowercase + ' '
str0    = 'methinks it is like a weasel'
N       = len(str0)

t0 = time.time()

score = 0
cnt   = 0
while score < 1.0:
    cnt += 1
    strNew  = stringNew(chrlist, N)
    score   = strcmp(str0, strNew)
    if cnt % 10000 == 0:
        print(score)
print(strNew)
print(score)
print(time.time() - t0)
