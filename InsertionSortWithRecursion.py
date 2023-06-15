a=[34,23,56,78,34,1,3,4,5,6,9,8,7,6,5,4,3,122,3,4,67,89,56,333]
def insert(last,array):
    key=array[last]
    while(last>0 and key<array[last-1]):
        array[last]=array[last-1]
        last-=1
    array[last]=key
def insertionSort(last,array):
    if(last==1):
        return insert(last, array)
    insertionSort((last-1), array)
    return insert((last), array)
insertionSort((len(a)-1),a)
print(a)     