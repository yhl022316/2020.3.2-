from pythonds.basic.stack import Stack
def divide2(desNumber):
    s=Stack()
    while desNumber>0:
         rem = desNumber % 2#取余数

         s.push(rem)#push()将一个新项放到栈的顶部
         desNumber=desNumber//2#  取整

    binString=""
    while not s.isEmpty():#isEmpty()测试是否为空
         binString=binString+str(s.pop())#pop()从栈中删除顶部项

    return binString
print(divide2(233))

print(11 // 2)


def divide3(desNumber1,base):
    a="0123456789ABCDEF"
    s=Stack()

    while desNumber1>0:
        b=desNumber1 % 2
        s.push(b)
        desNumber1=desNumber1//base
    c=""
    while not s.isEmpty():
        c=c+a[s.pop()]

    return c

print(divide3(20,16))
print(divide3(50,8))


def divideBase(desNumber,base):
    digits = '0123456789ABCDEF'
    s = Stack()

    while desNumber > 0:
        rem = desNumber % base
        s.push(rem)
        desNumber = desNumber // base

    binString = ""
    while not s.isEmpty():
        binString = binString + digits[s.pop()]

    return binString
print(divide3(20,16))
print(divide3(50,8))
