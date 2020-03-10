# def sequence_search(array, num):#array参数  是列表  num参数是
#     for i in range(len(array)):
#         if array[i] == num:
#             return i
#     return False
#
# array_0 = [23, 43, 12, 54, 65, 48]
# print(sequence_search(array_0, 12))

def sequential(alist,item):
    found=False
    pos=0

    while pos<len(alist) and not found:
        if alist[pos]==item:
            found=True
        else:
            pos=pos+1
    return found
testlist=[1,2,3,8,56,14]
print(sequential(testlist,14))
print(sequential(testlist,100))

def sum(list,base):
    found=False
    pos=0
    stop=False#让程序停止的条件
    while pos<len(list) and not found and not stop:
        if list[pos]==base:
            found=True
        else:
            if list[pos]>base:
                stop=True
            else:
                pos=pos+1
    return found
testlist=[1,5,9,15,21,26,33,40,59,62,75,100]
print(sum(testlist,101))

'''
有序列表
二分查找,每次都从剩余项的中间进行比对
1.确定中间项的位置是谁
'''
# def sum01(list,base,Conte):
#     found=False
#     pos=Conte
#     while pos
def binar(alist,item):
    found=False
    first=0
    last=len(alist)-1
    while first<=last and not found:
        #中间
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
        else:
            if item<alist[midpoint]:
                last=midpoint-1

            else:
                first=midpoint+1
    return found
testlist=[0,1,2,3,4,5,6,7,8,9]
print(binar(testlist,3))


#递归实现二分查找
def binary(alist,item):
    if len(alist)==0:
        return False
    midpoin=len(alist)//2
    if alist[midpoin]==item:
        return  True
    else:
        if alist[midpoin]>item:
            return binary(alist[:midpoin],item)
        else:
            return binary(alist[midpoin+1:],item)


def su(alist,item):
    found=False
    pos=0

    while pos<len(alist) and not found:
        if alist[pos]==item:
            found=True
        else:
            pos=pos+1
    return found




#二分查找 有序列表
'''
1.确定中间项是谁
'''
def center(alist,item):
    found=False
    first=0
    last=len(alist)-1

    while first<=last and not found:
        mid=(first+last)//2
        if alist[mid]==item:
            found=True
        else:
            if item<alist[mid]:
                last=mid-1
            else:
                first=mid+1
    return found



#递归二分查找
def bin(alist,item):
    if len(alist)==0:
        return False
    midn=len(alist)//2
    if alist[midn]==item:
         return True
    else:
        if alist[midn]>item:
            return bin(alist[:midn],item)
        else:
            return bin(alist[midn+1:],item)



