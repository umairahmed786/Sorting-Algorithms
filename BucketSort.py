import math
array=[5,2,9,6,23,-4]
def Scale(array):
    small=100000000
    for i in range(0,len(array)):
        if(array[i]<small):
            small=array[i]
    small=abs(small)
    for i in range(0,len(array)):
        array[i]+=small
    return array,small
def ReScale(array,number):
    for i in range(0,len(array)):
        array[i]-=number
    return array
def InsertionSort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key

def findLarge(array):
    large=array[0]
    for i in range(0,len(array)):
        if(array[i]>large):
            large=array[i]
    return large
def BucketSort(array):
    array,small=Scale(array)
    n=len(array)
    bucketArray=[]
    for i in range(0,len(array)):
        bucketArray.append([])
    maxDigitLen=len(str(findLarge(array)))
    diviser=1
    for i in range(0,maxDigitLen):
        diviser*=10
    for i in range(0,len(array)):
        array[i]/=diviser
    #print(array)
    for i in range(0,len(array)):
        bucketArray[math.floor(array[i]*len(array))].append(array[i])
    for i in bucketArray:
        InsertionSort(i)
    array=[]
    for i in bucketArray:
        array+=i
    for i in range(0,len(array)):
        array[i]=int(array[i]*diviser) 
    return ReScale(array, small)
print(BucketSort(array))
    