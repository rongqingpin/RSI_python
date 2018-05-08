def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)



# copy() necessary or not?

a = [1,2,3]
b = a[0]
# a[0] = a[1]
# a[1] = b
# a[1] = 4
b = 4
print(a)

a = [1,2,3]
b = a
b[0] = 4
print(a)

import numpy as np
a = np.ones((2,3))
a[0,:] = [1,2,3]
b = a[0,1]
# b = a[0,:]
b = 4
print(a)
