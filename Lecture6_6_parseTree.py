# define parse tree using stack and binary tree

# note: the current version requires putting parentheses wherever possible (input)

import operator

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

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

# parse tree for evaluating a fully parenthesized mathematical equation

def buildParseTree(fpexp):
    a = ''
    for i in fpexp:
        if not i.isdigit() and not i.isalpha():
            a += (' ' + i + ' ')
        else: a += i
    fplist = a.split()
    # fplist = fpexp.split()
    print(fplist)
    # sys.exit()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')', 'and', 'or', 'not']: # is a number
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/', 'and', 'or']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i in ['not']:
            parent = pStack.pop()
            currentTree = parent
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

# tree traversal: three methods

def preorder(tree): # the way you read a book
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree): # evaluate mathematical equation
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree): # writes the mathematical equation
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

# evaluate the mathematical equation

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, 'and':operator.and_, 'or':operator.or_, 'not':operator.not_}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        if leftC.key == '':
            return fn(evaluate(rightC))
        else:
            return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

def printexp(tree): # based on inorder traversal
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild())+')'
    return sVal


# evaluate the tree and test

import sys
# expr = '( (10+5) * 3 )'
# a = ''
# for i in expr:
#     if not i.isdigit():
#         a += (' ' + i + ' ')
#     else: a += i
# print(a.split())
# # print(expr.split())
# print('i'.isalpha())
# sys.exit()
# print((' ' + i + ' '))

pt = buildParseTree('((10 + 5) and 2)') #"( ( 10 + 5 ) * 3 )"
# postorder(pt)
# preorder(pt)
# inorder(pt)
print(printexp(pt))
print(evaluate(pt))
# print(postordereval(pt))
