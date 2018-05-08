import string
import random
import time

def chrNew(list0):
    return random.choice(list0)

def chrcmp(x, y):
    score0 = 1 if x == y else 0
    return score0

chrlist = string.ascii_lowercase + ' '
str0    = 'methinks it is like a weasel'
N       = len(str0)

t0 = time.time()

str2 = ''
cnt = 0
for i in range(N):
    scr0 = 0
    while scr0 != 1:
        ichr = chrNew(chrlist)
        scr0 = chrcmp(ichr, str0[i])
        cnt += 1
    str2 += ichr

print(str2)
print(cnt)

print(time.time() - t0)
