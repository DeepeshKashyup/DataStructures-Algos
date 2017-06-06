from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.V = v
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited[v] = True;
        print v,
        for w in self.graph[v]:
            if visited[w]==False:
                self.DFSUtil(w,visited)

    def fillOrder(self,s,visited,stack):
        visited[s] = True;
        for w in self.graph[s]:
            if visited[w]==False:
                self.fillOrder(w,visited,stack)
        stack = stack.append(s)
        
                

    def getTranspose(self):
        gr = Graph(self.V)
        for i in self.graph:
            #print i
            for j in self.graph[i]:
                gr.graph[j].append(i)
        return gr

    def printSCCs(self):
        visited = [False for i in range(self.V)]

        stack = []
        for u in range(self.V):
            if visited[u] == False:
                self.fillOrder(u,visited,stack)
        print stack

        gr = g.getTranspose()

        visited = [False]*(self.V)

        while stack:
            s = stack.pop()
            if visited[s]==False:
                gr.DFSUtil(s,visited)
                print ""



g = Graph(9)
#print g.V
##
##g.addEdge(1, 0)
##g.addEdge(0, 2)
##g.addEdge(2, 1)
##g.addEdge(0, 3)
##g.addEdge(3, 4)
g.addEdge(1,7)
g.addEdge(7,4)
g.addEdge(4,1)
g.addEdge(7,9)
g.addEdge(9,6)
g.addEdge(3,9)
g.addEdge(6,3)
g.addEdge(6,8)
g.addEdge(8,2)
g.addEdge(2,5)
g.addEdge(5,8)

print g.graph

visited = [False for i in range(g.V)]
#print visited
g.DFSUtil(0,visited)
gr= Graph(g.V)
gr.graph =g.getTranspose()
print gr.graph

#print
g.printSCCs()

