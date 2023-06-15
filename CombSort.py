array=[1,9,7,3,6,4,5,-8,-5,-2,-1]
starter=int(len(array)-1)
i=0
j=int(starter)
while starter>=1:
    if(array[i]>array[j]):
        temp=array[i]
        array[i]=array[j]
        array[j]=temp
    if(j==len(array)-1):
        starter=int(starter//1.3)
        j=starter
        i=0
    else:    
        i+=1
        j+=1
print(array)
    
    
    