''''
[1,3,5,7,9]
'''
def listSum(numlist):
    sum=0
    for i in  numlist:
        sum=sum+i

    return sum
print(listSum([1,3,5,7,9]))

#递归的三大定律
#1.递归算法必须有基本情况:基本情况是算法停止递归的条件,通常是足够小可以直接求解问题,在整数列表的和中,基本情况是长度为一的列表
#2.递归算法必须改变其状态并且向基本情况靠近
#3.递归算法必须以递归方式调用自身

def listsum2(numlist):
    if len(numlist)==1:
        return numlist[0]
    else:
        return numlist[0]+listsum2(numlist[1:])

print(listsum2([1,3,5,7,9]))