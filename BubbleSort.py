a=[1,9,2,8,4,8,5,6,7]
for i in range(1,len(a)):
    for k in range(len(a)-i):
        if(a[k]>a[k+1]):
            key=a[k+1]
            a[k+1]=a[k]
            a[k]=key
print(a)