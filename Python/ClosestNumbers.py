# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

def d(x,y):
    return math.sqrt((x-y)**2)

#n = int(raw_input())
#data = sys.stdin.readline()
#p = [int(x) for x in data.split(" ")]

n=4
p = [5,4,3,2]

best = 9999
best_pair = ()
p.sort()
print p
for i in range(0,n-1):
    x= p[i]
    y= p[i+1]
    dist = d(x,y)
    if(dist<best):
        best_pair = (x,y)
        best = dist
    elif(dist==best):
        best_pair = best_pair + (x,y)

for x in best_pair:
    print x,
