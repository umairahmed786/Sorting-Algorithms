a=[3,1,9,7,2,8,4]
for i in range(len(a)-1):
    for j in range(i,len(a)):
        if(a[j]<a[i]):
            key=a[j]
            a[j]=a[i]
            a[i]=key
print(a)