
##m = input()
##
##arr = [int(x) for x in raw_input().strip().split()]

import random

arr = [5, 8, 1, 3, 7, 9, 2,6]
i=4

def RSelect(arr,i):
    print "inside Rselect"
    print arr
    n = len(arr)
    if n==1:
        return arr
    else:
        pivot = random.randint(0,n-1)
        #print "random pivot is ",pivot
        j,arr = partition(arr,pivot)
        print "value of j",j,"\t order statistic is ",i
        #print arr
        if j==i:
            return arr
        elif j>i:
            RSelect(arr[0:j],i)
        elif j<i:
            RSelect(arr[j+1:n],i-j-1)

def partition(arr,pivot):
    print "inside partition "
    p = arr[pivot]
    print arr
    print "random pivot is ",p
    i = 0
    for j in range(i,len(arr)):
        #print i,j
        if arr[j]<p:
            swap(arr,i,j)
            if i==pivot:
                pivot = j
            i=i+1
            #print arr
    swap(arr,i,pivot)
    print "end of partition pos ", arr
    print "value of i",i,"\tpos of pivot",pivot
    return i,arr

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j]=temp

x= RSelect(arr,i)
#print x

