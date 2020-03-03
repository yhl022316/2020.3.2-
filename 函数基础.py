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


#函数嵌套
def demo1():
    print('*'*50)
    print('/'*50)
demo1()
def demo2():
    print('='*50)
    demo1()#函数的嵌套   代码从上往下先执行demo1,
    # 在执行demo2,最后执行在demo2中嵌套的demo1
demo2()


def print_lien(hare,char):
    pass
    print(hare*char)
print_lien('+',25)

def print_lnes(char,hare):

    row=0
    while row<5:
        print_lien(char,hare)

        row+=1
    
print_lnes('-',5)





