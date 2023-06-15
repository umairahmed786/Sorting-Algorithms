a=[9,2,4,3,2,3,3,9,6,78,23,56,78,34,1,3,4,5,6,9,8,7,6,5,4,3,122,3,4,67,89,56,333]
def Merge(start,m,end,array):
    n1=m-start+1
    n2=end-m
    l=[None]*(n1)
    r=[None]*(n2)
    for i in range(0,n1):
        l[i]=array[start+i]
    for i in range(0,n2):
        r[i]=array[m+1+i]
    i=0
    j=0
    k=start
    while i<n1 and j<n2:
        if(l[i]>r[j]):
            array[k]=r[j]
            j+=1
            k+=1
        else:
            array[k]=l[i]
            i+=1
            k+=1
    while i<n1:
        array[k]=l[i]
        i+=1
        k+=1
    while j<n2:
        array[k]=r[j]
        j+=1
        k+=1
def MergeSort(startInd,endInd,array):
    if(startInd<endInd):
        m=((endInd-1)+startInd)//2
        MergeSort(startInd, m, array)
        MergeSort(m+1, endInd, array)
        Merge(startInd,m,endInd,array)
MergeSort(0, len(a)-1, a)
print(a)