#a和b的交换
a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)

#
#冒泡排序
def bubble(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
alist=[1,8,5,78,36,55,45,100]
bubble(alist)
print(alist)

#短冒泡排序
def bubblesort(alist):
    flag=True
    passnum=len(alist)-1
    while passnum>0 and flag:
        flag=False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                flag=True
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
        passnum=passnum-1
alist=[1,8,5,78,36,55,45,100]
bubblesort(alist)
print(alist)








#选择排序
def selection(alist):
    for fillsort in range(len(alist)-1,0,-1):
        maxpos=0
        for location in range(1,fillsort+1):
            if alist[location]>alist[maxpos]:
                maxpos=location

        temp=alist[fillsort]
        alist[fillsort]=alist[maxpos]
        alist[maxpos]=temp
alist=[54,65,32,78,51,12,57,67]
print(alist)
selection(alist)
print(alist)

#插入排序
def insertionsort(alsit):
    for i in range(1,len(alsit)):
        curren=alist[i]
        pos=i
        while pos>0 and alist[pos-1]>curren:
            alist[pos]=alist[pos-1]
            pos=pos-1

        alist[pos]=curren
alist=[54,65,32,78,51,12,57,67]
insertionsort(alist)
print(alist)

#希尔排序
def shell(alist):
     sublistcount=len(alist)//2
     while sublistcount >0:
         for startposition in range(sublistcount):
             gapinsert(alist,startposition,sublistcount)

         print('alist',alist)
         sublistcount=sublistcount//2
def gapinsert(alist,start,gap):
    for i in  range(start+gap,len(alist),gap):
        curren=alist[i]

        pos=i
        while pos >=gap and alist[pos-gap]>curren:
            alist[pos]=alist[pos-gap]
            pos=pos-gap

        alist[pos]=curren
alist=[54,26,93,17,77,31,44,55,20]
shell(alist)
print(alist)