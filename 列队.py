#栈的特点: 后进先出   低端1,2,3,4,5 顶端     栈 对于设计计算解析表达式算法非常有用
#列队的特点:先进先出
#列队练习

class Printer:
    # 初始化参数：设置打印机的速率（每分钟5页还是10页）
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印机的速率
        self.currentTask = None  # 空闲状态
        self.timeRemaining = 0  # 打印任务需要的时间为0,为空闲状态

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pagerate


import random


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


from pythonds.basic.queue import Queue


# newPrintTask 决定是否创建一个新的打印任务。1个小时之内20任务打印完成，打印任务每180秒到达一次
def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)  # 初始化打印机
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)

    print("平均等待时间为：%6.2f" % averageWait)


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 20)  # 一个小时，速率5页