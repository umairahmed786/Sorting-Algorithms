
def quickSort(array,low,high):
    if(low<high):
        p=partition(array,low,high)
        quickSort(array,low,p-1)
        quickSort(array,p+1,high)
    return array

def partition(array,low,high):
    pivot=array[high]
    i=(low-1)
    for j in range(low,high):
        if(array[j]<pivot):
            i+=1
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
            
            
    temp=array[i+1]
    array[i+1]=pivot
    array[high]=temp
    return(i+1)

array=[5,2,3,3,9,6,78,23,56,78,34,1,3,4,5,6,9,8,7,6,5,4,3,122,3,4,67,89,56,333]

print(quickSort(array,0,len(array)-1))

#print(array)