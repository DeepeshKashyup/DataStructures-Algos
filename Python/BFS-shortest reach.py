# Enter your code here. Read input from STDIN. Print output to STDOUT
class queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        x=""
        for i in self.items:
            x=x+str(i)+" "
        return x

q= input()

def BFS(s,adjL):
    q= queue()
    q.enqueue(s)
    dist = [0 for i in range(len(adjL))]
    notVisited = [True for i in range(len(adjL))]
    notVisited[s]=False
    #print q.dequeue()
    while not q.isEmpty():
        u=q.dequeue()
        for w in adjL[u]:
            if notVisited[w]:
                dist[w]= dist[u]+6
                q.enqueue(w)
                notVisited[w]=False
            
    #print s,adjL
    return dist

while(q>0):
    mn = raw_input().strip().split()
    v=int(mn[0])
    e=int(mn[1])
    adjL = [[] for i in range(v+1)]
    #print adjL
    #print q,v,e
    while(e>0):
        edge = raw_input().strip().split()
        u = int(edge[0])
        w = int(edge[1])
        adjL[u].append(w)
        adjL[w].append(u)
        e =e-1
    #print adjL
    s = input()
    x=BFS(s,adjL)
    for i in range(len(x)):
        if i==s or i==0:
            continue;
        if x[i]==0:
            x[i]= -1
        print x[i],
    print
    q=q-1
