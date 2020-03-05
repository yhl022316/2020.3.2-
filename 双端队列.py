#Deque的抽象数据类型和Python实现
# *Duque(),创建一个空的Duque,不需要参数,返回空的Duque
# addFront(item)将心的项添加到Duque尾部,需要item作为参数,不返回任何内容



from pythonds.basic.deque import Deque
def plaCheckaer(astring):
    chardeque=Deque()
    for ch in astring:
        chardeque.addRear(ch)
    flag=True
    while chardeque.size()>1 and flag:
        frist=chardeque.removeFront()
        last=chardeque.removeRear()

        if frist!=last:
            flag=False
    return flag
print(plaCheckaer("山西运煤车煤运西山"))
print(plaCheckaer("Python"))

