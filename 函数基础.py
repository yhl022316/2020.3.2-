yhl='杨昊霖'
#形参
# #把实参调入到形参
def name(name):
    # print("我是杨昊霖")
    # print("你是谁?")
    # print(yhl)
    print(name)
name('你管我是谁呢')#实参


def sum_num(num,num1):

    return num+num1
a=sum_num(22,55)#调用函数必须要有变量a来接受函数  最后print(a)打印结果
print(a)


a=[0]*26
print(a)



print(ord('a'))
ord('b')-ord('a')#表示  b的角标

#排序  sort()
def sum(s1,s2):
    a=list(s1)
    b=list(s2)


    a.sort()
    b.sort()
    print(a)
    print(b)
sum('abcdef','facbed')

