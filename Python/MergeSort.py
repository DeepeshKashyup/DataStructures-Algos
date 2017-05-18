
def merge_sort(a,p,r):
    if p < r:
        q = (p+r-1)/2
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)

def merge(a,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    print p,q,r
    for i in range(0,n1):
        L.append(a[p+i])
    for i in range(0,n2):
        R.append(a[q+1+i])
    L.append(99)
    R.append(99)
##    print L
##    print R
##    print p,r+1
    i = 0
    j = 0
    for k in range(p,r+1):
        if(L[i] < R[j]):
            a[k] = L[i]
            i = i +1
        elif(R[j]<L[i]):
            a[k] = R[j]
            j = j + 1
    print a

a = [5,4,1,7,2,6,3]

#a = raw_input().split()
merge_sort(a,0,len(a)-1)

print a
