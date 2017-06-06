class stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        n = len(self.items)-1
        return self.items.pop(n)

    def peek(self):
        n = len(self.items)-1
        return self.items[n]

    def isEmpty(self):
        return self.items==[]

    def __str__(self):
        l = []
        for x in self.items:
            l.append(str(x))
        return " ".join(l)



adjL = [[1,2,3],[0,4],[0,5],[0,6],[1,7],[2,7],[3,7],[4,5,6]]

def DFS(s,g,adjL):
    k = stack()
    # step : counts the no. of steps taken to reach the goal
    step = 0
    ## dist : counts the distance of each node from source
    dist = [0 for i in range(len(adjL))]
    ## not visited : by default all nodes are not visited
    notVisited = [True for i in range(len(adjL))]

    k.push(s)
    notVisited[s] = False
    while not k.isEmpty():
        ## u,w are the pair of vertices forming an edge
        u= k.pop()
        for w in adjL[u]:
            if notVisited[w]:
                notVisited[w]= False
                dist[w] = dist[u] + 6
                k.push(w)
                step = step + 1
                print "Node :",w," Steps :",step
                if g==w:
                    break
    
    return dist            


s = input()
g = int(input())
x=DFS(s,g,adjL)
for i in range(len(x)):
    if i==s or i==0:
        continue;
    if x[i]==0:
        x[i]= -1
    print x[i],
print

