#抽象数据类型,adt或者节点的表示方式
class BinarTree:
    def __init__(self,rootobj):
        self.key=rootobj
        #新树的根节点
        self.leftChild=None
        self.rightChild=None

    def insertleft(self,newMode):
        if self.leftChild==None:
            self.leftChild=BinarTree(newMode)
        else:
            temp=BinarTree(newMode)
            temp.leftChild=self.leftChild
            self.leftChild=temp

    def insertRight(self,newMode):
        if self.rightChild==None:
            self.rightChild=BinarTree(newMode)
        else:
            temp=BinarTree(newMode)
            temp.rightChild=self.rightChild
            self.rightChild=temp

    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
r = BinarTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertleft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())



from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+','-','*',"/"]:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else: raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv
     }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
         return parseTree.getRootVal()


pt = buildParseTree('( 3 + ( 4 * 5 ) )')
 # pt.postorder()

print(evaluate(pt))


