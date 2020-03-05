from pythonds.basic.stack import Stack
def divide2(desNumber):
    s=Stack()
    while desNumber>0:#输入的十进制数字以及多次除二操作之后的数字必须>0
         rem = desNumber % 2 #算出余数
         s.push(rem)#将算出的雨水放入栈中
         desNumber=desNumber//2#算出来的整数商进行下一次循环

    binString=""
    while not s.isEmpty():#栈不是空的状态
         binString=binString+str(s.pop())#取出来 pop()

    return binString
print(divide2(233))

# def divide2(desNumber):
#     s=Stack()
#     while desNumber>0:
#          rem = desNumber % 2#取余数
#
#          s.push(rem)#push()将一个新项放到栈的顶部
#          desNumber=desNumber//2#  取整
#
#     binString=""
#     while not s.isEmpty():#isEmpty()测试是否为空
#          binString=binString+str(s.pop())#pop()从栈中删除顶部项
#
#     return binString
# print(divide2(233))
