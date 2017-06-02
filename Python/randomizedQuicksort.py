import random
#arr = [3,8,2,5,1,4,7,6,9]
arr = [5, 8, 1, 3, 7, 9, 2,6]
#print arr


def quicksort(arr,start,end):
    #print arr[start:end]
    n = len(arr[start:end])
    if n <= 1:
        return
    else:
        pivot = random.randint(start,end-1)
        #print pivot
        p = partition(arr,start,end,pivot)
        #print arr[p:end]
        quicksort(arr,start,p)
        quicksort(arr,p+1,end)
        

def partition(arr,l,r,pivot):
    print l,r
    print arr[l:r]
    p = arr[pivot]
    print "pivot element" ,p
    i = l
    for j in range(i,r):
        print "i is :",i,"\t j is :",j
        #print j,i,p
##        if(arr[j]==p):
##            i=i+1
        if arr[j]<p:
            if(i==pivot):
                pivot = j
            swap(arr,i,j)
            print arr[l:r]
            i = i+1
            
    temp = arr[i]
    arr[i] = arr[pivot]
    arr[pivot] = temp
    print arr
    print i
    return i

def swap(arr,i,j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp

quicksort(arr,0,len(arr))

print arr
    
