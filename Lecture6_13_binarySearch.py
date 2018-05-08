class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    # override 'for i in x'
    def __iter__(self):
        return self.root.__iter__()

    # add a new value
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        # a private helper function
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)
        else:
            currentNode.replaceNodeData(key, val)#, currentNode.leftChild, currentNode.rightChild, currentNode.parent

    # enables accessing in the form of dictionary
    def __setitem__(self,k,v):
        self.put(k,v)

    # read a value
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                   return res.payload
            else:
                   return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    # enables accessing in the form of dictionary
    def __getitem__(self,key):
        return self.get(key)

    # enables 'in' operation
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False

    # delete a key and its value
    def delete(self,key):
        if self.size > 1:
          nodeToRemove = self._get(key,self.root)
          if nodeToRemove:
              self.remove(nodeToRemove)
              self.size = self.size-1
          else:
              raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
          self.root = None
          self.size = self.size - 1
        else:
          raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        # enables 'del' operation
        self.delete(key)

    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
            else:
               currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,currentNode.leftChild.payload,currentNode.leftChild.leftChild,currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,currentNode.rightChild.payload,currentNode.rightChild.leftChild,currentNode.rightChild.rightChild)


class TreeNode:

    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value):#,lc,rc,pr
        self.key = key
        self.payload = value
        # self.leftChild = lc
        # self.rightChild = rc
        # self.parent = pr # neccessory?
        # self.successor = sc # neccessory?
        # if self.hasLeftChild():
        #     self.leftChild.parent = self
        # if self.hasRightChild():
        #     self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else: # not used for delete, used for inorder traversal
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild(): # not visited
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else: # goes here directly
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

def inorder(tree):
    if tree != None:
        istart = tree.root.findMin()
        print(istart.payload)
        inext = istart.findSuccessor()
        while inext:
            print(inext.payload)
            inext = inext.findSuccessor()


# last case of find successor
# spliceOut doesn't work for self has both children?

mytree = BinarySearchTree()
mytree[17]="17"
mytree[5]="5"
mytree[35]="35"
mytree[2]="2"
mytree[5] = 'in' # test replace
mytree[11] = '11'
mytree[29] = '29'
mytree[38] = '38'
mytree[9] = '9'
mytree[16] = '16'
mytree[7] = '7'
mytree[8] = '8'
mytree[18] = '18'

# # print(len(mytree))
# # del mytree[11]
# del mytree[35]
# # for i in mytree:
# #     print(mytree[i])
# print(mytree.root.key)
print(mytree.root.leftChild.payload)
print(mytree.root.leftChild.leftChild.payload)
# print(mytree.root.rightChild.leftChild.key)
# # if mytree.root.rightChild.hasLeftChild: print('here')

# inorder(mytree)
