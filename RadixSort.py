array=[329,457,657,839,436,720,255]

def R(array):
    def CountingSort(array,k,large):
        b=[0]*len(array)
        c=[0]*10
        for i in array:
            c[(i//k)%10]+=1
        for i in range(1,len(c)):
            c[i]+=c[i-1]
        for i in range(len(array)-1,-1,-1):
           b[c[((array[i]//k)%10)]-1]=array[i]
           c[(array[i]//k)%10]=c[(array[i]//k)%10]-1
        return(b)
    temp=1
    large=-1
    for i in range(0,len(array)):
        if(large<int(array[i])):
            large=int(array[i])
    for i in range(0,len(str(large))):
        array=CountingSort(array,temp,large)
        temp*=10
    return array
