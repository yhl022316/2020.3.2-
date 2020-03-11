def sort(alist):
    for word in range(len(alist)-1,0,-1):
        for i in range(word):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
alist=[54,59,3,12,1,15,66,8,89,101]
sort(alist)
print(alist)



#短冒泡排序  当列表遍历过程中没有交换,则证明列表已经排序,
            # 这时候可以修改 冒泡排序提前停止

def sum(alist):
    flag=True
    passnum=len(alist)-1
    while passnum>0 and flag:
        flag = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                flag=True
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
        passnum=passnum-1
alist=[54,59,3,12,1,15,66,8,89,101]
sum(alist)
print(alist)

#选择排序   每次遍历列表只做已一次交换,选择遍历会在遍历时找最大的值,并且在遍历完后会放在核实的位置
def sick(alist):
    for fillsort in range(len(alist)-1,0-1):
        max=0
        for location in range(1,fillsort+1):
            if alist[location]>alist[max]:
                max=location
        temp=alist[fillsort]
        alist[fillsort]=alist[max]
        alist[max]=temp
alist=[54,59,3,12,1,15,66,8,89,101]
sick(alist)
print(sick)



