a=[1,2,3,4,5,6,7,8,1,2,3,-1]
def InsertionSort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key

InsertionSort(a)
print(a)
        
        
    