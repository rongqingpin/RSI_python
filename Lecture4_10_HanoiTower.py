# version 1

# def moveTower(height,fromPole, toPole, withPole):
#     if height >= 1:
#         moveTower(height-1,fromPole,withPole,toPole)
#         moveDisk(fromPole,toPole)
#         moveTower(height-1,withPole,toPole,fromPole)
#
# def moveDisk(fp,tp):
#     print("moving disk from",fp,"to",tp)
#
# moveTower(3,"A","B","C")


# version 2: use stack to keep track of disk location

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    a = fp.pop()
    tp.push(a)
    # print("moving disk from",fp,"to",tp)

A = Stack()
A.push(3); A.push(2); A.push(1)
B = Stack()
C = Stack()
moveTower(3,A,B,C)
print([A.pop() for i in range(A.size())])
print([B.pop() for i in range(B.size())])
print([C.pop() for i in range(C.size())])
