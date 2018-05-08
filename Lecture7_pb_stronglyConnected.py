class Vertex:
    def __init__(self,key,color = 'white', predecessor = None, startTime = 0, finishTime = 0):
        self.id = key
        self.connectedTo = {}
        self.record = color
        self.predecessor = None
        self.start = startTime
        self.finish = finishTime

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setColor(self, color):
        self.record = color

    def getColor(self):
        return self.record

    def setPred(self, aVertex):
        self.predecessor = aVertex if aVertex != -1 else None

    def setDiscovery(self, startTime):
        self.start = startTime

    def setFinish(self, finishTime):
        self.finish = finishTime


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def transposition(self):
        oldList = []
        for aVertex in self:
            for bVertex in aVertex.connectedTo:
                oldList.append([aVertex, bVertex, aVertex.getWeight(bVertex)])
            aVertex.connectedTo = {}
        for i in oldList:
            self.addEdge(i[1].id, i[0].id, i[2])

    def dfs_sorted(self):
        self.time = 0 # reset time
        sortedList = []
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
            sortedList.append((aVertex.finish, aVertex))
        sortedList = sorted(sortedList, reverse = True)
        for i, aVertex in sortedList:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)


import sys

def buildGraph(g, vertices, edges):
    for i in vertices: g.addVertex(i)
    for i, j in edges: g.addEdge(i, j)

'''
(start, finish, v)
if new.start > [0] and new.finish < [1]: add to this tree
elif: new.start < [0] and new.finish > [1]: add to this tree & promote as parent
else: add a new tree
'''
def SCC(g):
    forests = []
    for v in g:
        istart = v.start; ifinish = v.finish
        if not forests: forests.append([(istart, ifinish, v.id)])
        for itree in forests:
            start0 = itree[0][0]; finish0 = itree[0][1]
            if istart > start0 and ifinish < finish0:
                itree.append((istart, ifinish, v.id))
            elif istart < start0 and ifinish > finish0:
                itree.insert(0, (istart, ifinish, v.id))
            else:
                forests.append([(istart, ifinish, v.id)])
    return forests


# using the example in 7.18
g = DFSGraph()
vertices = [chr(i) for i in range(ord('A'), ord('J'))]
edges = [('A', 'B'), ('B', 'C'), ('B', 'E'), ('C', 'F'), ('C', 'C'), \
         ('D', 'B'), ('D', 'G'), ('E', 'A'), ('E', 'D'), ('F', 'H'), \
         ('G', 'E'), ('H', 'I'), ('I', 'F')]
buildGraph(g, vertices, edges)
# for v in g:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))

# calculate the finish time, transpose, dfs again
g.dfs()
g.transposition()
g.dfs_sorted()
# for v in g:
#     print("( %s , %d, %d )" % (v.id, v.start, v.finish))
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))

# show the trees
print(SCC(g))
