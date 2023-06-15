array=[5,9,3,1,7,4,6,-8]
def ShellSort(array):
    gap=len(array)//2
    while gap>=1:
        for j in range(gap,len(array)):
            temp=array[j]
            i=j
            while (i>=gap and array[i-gap]>temp):
                array[i]=array[i-gap]
                i=i-gap
            array[i]=temp
        gap=gap//2
    return array
print(ShellSort(array))
        