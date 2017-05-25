import sys

n =  input()
data = sys.stdin.readline()
l = [int(x) for x in data.split(" ")]
l.sort()
print l
