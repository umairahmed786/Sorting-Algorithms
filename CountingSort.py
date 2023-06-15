array=[2,5,3,0,2,100000,0,3]
def CountingSort(array):
    large=-1
    b=[0]*len(array)
    for i in range(0,len(array)):
        if(large<array[i]):
            large=array[i]
    c=[0]*(large+1)
    for i in array:
        c[i]+=1
    for i in range(1,len(c)):
        c[i]+=c[i-1]
    for i in range(len(array)-1,-1,-1):
       b[c[array[i]]-1]=array[i]
       c[array[i]]=c[array[i]]-1
    return(b)
        
print(CountingSort(array))