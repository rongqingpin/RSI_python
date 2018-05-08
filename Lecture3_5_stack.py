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


a = Stack()
a.isEmpty()
a.push(1)
a.push(2)
a
a.peek()


b = 'apple'
c = list(b)
c
c.reverse()
c
d = ''
for i in c: d += i
d
