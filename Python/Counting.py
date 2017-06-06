

##k = input()
##n = [int(x) for x in raw_input().strip().split()]

k = 5
A = [2,5,3,0,2,3,0,3]

B = [0 for x in range(len(A))]

def countingSort(A,B,k):
    c = [0 for x in range(k+1)]

    for i in range(len(A)):
        c[A[i]] = c[A[i]]+1

    #print c 
    for i in range(1,k+1):
        c[i] = c[i]+c[i-1]
    #print c

    for j in reversed(range(len(A))):
        B[c[A[j]]-1] = A[j]
        #print B
        c[A[j]]=c[A[j]]-1
    return B

op = countingSort(A,B,k)
print op
