# general depth first search, O(vertex + edge)


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


import sys

# test the algorithm with example in 7.15
g = DFSGraph()
for i in range(ord('A'), ord('G')):
    g.addVertex(chr(i))
g.addEdge('A', 'B'); g.addEdge('A', 'D')
g.addEdge('B', 'C'); g.addEdge('B', 'D')
g.addEdge('D', 'E'); g.addEdge('E', 'F'); g.addEdge('F', 'C')
# for v in g:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))

g.dfs()
for v in g:
    print("( %s , %d, %d )" % (v.id, v.start, v.finish))
