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

#q= input()

def BFS(s,g,adjL):
    step = 0
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
                #distance between two nodes assumed to be 6
                dist[w]= dist[u]+6
                q.enqueue(w)
                notVisited[w]=False
                step = step+1
                print "Node :",w," Step:",step
                if w == g:
                    break;
            
    #print s,adjL
    return dist


##mn = raw_input().strip().split()
##v=int(mn[0])
##e=int(mn[1])
##adjL = [[] for i in range(v+1)]
adjL = [[1,2,3],[0,4],[0,5],[0,6],[1,7],[2,7],[3,7],[4,5,6]]
#print adjL
#print q,v,e

## Code to read pair of vertices forming edges and storing in adjacency list
##while(e>0):
##    edge = raw_input().strip().split()
##    u = int(edge[0])
##    w = int(edge[1])
##    adjL[u].append(w)
##    adjL[w].append(u)
##    e =e-1
#print adjL

s = input()
g = input()
x=BFS(s,g,adjL)
for i in range(len(x)):
    if i==s or i==0:
        continue;
    if x[i]==0:
        x[i]= -1
    print x[i],
print

