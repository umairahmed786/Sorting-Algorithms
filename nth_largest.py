import random

def find_large(arr, k):
    if len(arr)>1:
        # random_number=random.randrange(0, len(arr)-1)
        random_number=len(arr)-1
        number=arr[random_number]
        index=0



        for i in range(0,len(arr)):
            if(arr[i]>number):
                temp=arr[index]
                arr[index]=arr[i]
                arr[i]=temp
                index+=1
        
        # random_number=arr.index(number)
        temp=arr[index]
        arr[index]=number
        arr[random_number]=temp


        if(index+1==k):
            return arr[index]
        elif(index+1>k):
            return find_large(arr[:index], k)
        else:
            return find_large(arr[index+1:], k-(index+1))

    else:
        return arr[0]





print(find_large([4,2,7,8,5,6,9], 7))


