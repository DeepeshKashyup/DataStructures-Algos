
#arr = [3,8,2,5,1,4,7,6,9]
arr = [5, 8, 1, 3, 7, 9, 2]
#print arr


def quicksort(arr,start,end):
    #print arr[start:end]
    n = len(arr[start:end])
    if n <= 1:
        return
    else:
        p = partition(arr,start,end)
        print arr[p:end]
        quicksort(arr,start,p-1)
        quicksort(arr,p+1,end)
        

def partition(arr,l,r):
    #print l,r
    #print arr[l:r]
    p = arr[l]
    i = l+1
    for j in range(i,r):
        #print j,i,p
        if arr[j]<p:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            print arr
            i = i+1
    temp = arr[i-1]
    arr[i-1] = arr[l]
    arr[l] = temp
    print arr
    #print i-1
    return i-1

quicksort(arr,0,len(arr))

print arr
    
