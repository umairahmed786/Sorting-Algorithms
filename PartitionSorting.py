# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 22:41:45 2022

@author: Umair Ahmed
"""

name=[0,2,0,1,2,0,1,2,1,1,0,2,1,0,0,2,1,0,2,0,1,2,0,1,2,1,1,0,2,1,0,0,2,1]
left=0
right=len(name)-1
i=0
pivot=1
while i<right:
    if (int(name[i])>pivot):
        temp=name[i]
        name[i]=name[right]
        name[right]=temp
        right-=1
    elif(int(name[i])==pivot):
        i+=1
    else:
        temp=name[i]
        name[i]=name[left]
        name[left]=temp
        i+=1
        left+=1
print(name)