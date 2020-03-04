
#抽象数据类型
#1. 栈抽象类型的数据实现
class Stack:
    def __init__(self):
        self.items=[]

    def IsEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

from pythonds.basic.stack import  Stack

s=Stack()
print(s.isEmpty())
s.push(4)
s.push('lalala')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(10.9)
print(s.pop())
print(s.pop())
print(s.size())


#()匹配

def parCheck(symbolsting):#假设symbolsting是"(())"
    s=Stack()
    flag=True
    index=0
    while index<len(symbolsting)and flag:
        symbol = symbolsting[index]
        if symbol=="(":
            s.push(symbol)

        else:
            if s.isEmpty():#isEmpty()测试栈是否为空。不需要参数，返回布尔值
                flag=False


            else:
                s.pop()#pop()从栈中删除顶部项。它不需要参数并返回item。栈被修改

        index=index+1

    if flag and s.isEmpty():
        return True
    else:
        return False



print(parCheck('(())'))
print(parCheck('((())'))


# def parChecker(symblolString):
#     s = Stack()
#     flag = True
#     index = 0
#     while index<len(symblolString) and flag:
#         symbol = symblolString[index]
#         if symbol == "(":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 flag = False
#             else:
#                 s.pop()
#         index = index + 1
#     if flag and s.isEmpty():
#         return True
#     else:
#         return False
# print(parChecker('(())'))
# print(parChecker('((())'))
