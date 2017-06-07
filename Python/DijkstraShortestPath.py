from collections import defaultdict

class graph:

    def __init__(self,v):
        self.V=v
        self.graph = defaultdict(dict)
        self.q = []
        self.dist = [float('inf')]*self.V
        self.path = [[] for _ in range(v)]

    def enqueue(self,item):
        self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)
    
    def addEdge(self,tail,head,length):
        self.graph[tail][head] = length


    def DijkstraSP(self,s):

        visited= [False]*self.V
        visited[s]=True
        
        self.dist[s]= 0
        self.path[s].append(s)
        self.enqueue(s)

        while not self.q == []:
            u = self.dequeue()
            for w in self.graph[u]:
                #print 'u:',u,'\tw:',w
                if(self.dist[w] > self.dist[u]+self.graph[u][w]):
                    self.dist[w] = self.dist[u]+self.graph[u][w]
                    self.path[w]=[]
                    for x in self.path[u]:
                        self.path[w].append(x)
                    self.path[w].append(w)
                #print dist
                #print self.path

                self.enqueue(w)
                visited[w]= True
##
##        print self.dist
##        print self.path


g = graph(4)
g.addEdge(0,1,1)
g.addEdge(0,2,4)
g.addEdge(1,2,2)
g.addEdge(1,3,6)
g.addEdge(2,3,3)

print g.graph
g.DijkstraSP(0)
print g.dist
print g.path

