

def count(A,p,r):
    if (r-p+1) == 1:
        return 0
    else:
        q= (p+r-1)/2
        #print p,q,r
        x = count(A,p,q)
        y = count(A,q+1,r)
        z = countSplitInv(A,p,q,r)
    return x+y+z

def countSplitInv(A,p,q,r):
    #print p,q,r
    n1 = q-p+1;
    n2 = r-q;
    L = []
    R = []
    for i in range(0,n1):
        L.append(A[p+i])
    for i in range(0,n2):
        R.append(A[q+1+i])

    #print L
    #print R
    L.append(float('inf'))
    R.append(float('inf'))

    count = 0
    i=0
    j=0
    for k in range(p,r+1):
        if(L[i]<R[j]):
            A[k] = L[i]
            i=i+1
        elif(R[j]<L[i]):
            count = count +(n1-i)
            #print R[j], L[i:n1]
            A[k] = R[j]
            j=j+1
        else:
            A[k] = L[i]
            i=i+1
            
    #print A
    return count

#A = [1,3,5,2,4,6]
A=[2,1,3,1,2]

print count(A,0,len(A)-1)
            
