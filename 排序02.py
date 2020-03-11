#归并排序
def mergesort(alist):
    print('拆分的列表',alist)
    if len(alist)>1:
        mid=len(alist)//2
        leftHalf=alist[:mid]
        rightHalf=alist[mid:]

        mergesort(leftHalf)
        mergesort(rightHalf)

        i=0
        j=0
        k=0
        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i]<rightHalf[j]:
                alist[k]=leftHalf[i]
                i=i+1
            else:
                alist[k]=rightHalf[j]
                j=j+1

            k=k+1

        while i<len(leftHalf):
            alist[k]=leftHalf[i]
            i=i+1
            k=k+1
        while j<len(rightHalf):
            alist[k]=rightHalf[j]
            j=j+1
            k=k+1

        print("合并:",alist)

alist=[54,26,93,17,77,31,44,55,20]
mergesort(alist)
print(alist)


# #快速排序
def quicksort(alist):
    quickSortHelper(alist, 0, len(alist)-1)
def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue=alist[first]
    leftMark=first+1
    rightMark=last

    done=False
    while not done:
        while leftMark<=rightMark and alist[leftMark]<=pivotvalue:
            leftMark=leftMark+1
        while alist[rightMark]>=pivotvalue and rightMark>=leftMark:
            rightMark=rightMark-1
        if rightMark<leftMark:
            done=True
        else:
            temp=alist[leftMark]
            alist[leftMark]=alist[rightMark]
            alist[rightMark]=temp

    temp=alist[first]
    alist[first] = alist[rightMark]
    alist[rightMark] = temp

    return rightMark
alist=[54,26,93,17,77,31,44,55,20]
quicksort(alist)
# print(alist)


