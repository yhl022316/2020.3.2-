"""
乱序字符串是指一个字符串指示另一个字符串重新排列
前提:字符串是26个小写字符集合组成  长度相同
比如: Python   onthpy
目的:
写一个布尔函数(返回布尔值的函数)

"""
# def ang(s1,s2):
#     if len(s1)!=len(s2):
#         return False
# a=ang('hjkjlkjl','huhkjkjjlkjlkj')
# print(a)




#穷举法:排除,因为如果字符串过长,我们的循环将写到无数次



# 检查第一个字符串是不是出现在第二个字符串中
def sum1(s1,s2):#定义一个函数,传入两个字符串
    alist=list(s2)
    alistl=list(s1)
    pos1=0#角标
    flag=True#标志,可以检测到第二个字符串中有第一个字符串就返回True
#从字符串第一个位置去检查,检查到在第二个字符串中检测到了这个字符为止
    while flag and pos1<(len(s1)):#从这个while循环中取出一个字符,假设为a,这
# 时 pos=0,从pos2下标为零的字符开始检查,如果pos1的字符与pos2的字符一样,则found返回True,不一样,
# 则else pos1比较pos2的下一个pos2=pos2+1
        pos2=0
        found=False
        while pos2<(len(s2)):
            if alistl[pos1]==alist[pos2]:
                found=True
            else:
                pos2=pos2+1#否则接着去循环,进入到下一个循环里去,

        if found:#在found变为True的时候,也就是说pos1的字符在pos2中,执行这个if
            alist[s2]=None
            pos1=pos1+1#因为当pos1在pos2中时,要执行下一个pos1和pos2的比较,所以,pos1=pos1+1是开始下一次的循环
        else:
            flag=False
    return flag
print(sum1("hjkk","jkljlkl"))

# 计数和比较法
# 计算每个字符出现的次数
def sum2(s1,s2):

    a1=[0]*26#记录s1字母出现的次数
    a2=[0]*26#记录s2字母出现的次数
    #ord  ()  返回字母在阿斯克码中的位置
    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')#当前位置字符i减去ord('a')就能得到当前位置字符i的角标
        a1[pos]=a1[pos]+1
    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        a2[pos]=a2[pos]+1
    # flag=True
    count=0#s1与s2比对完成后 ,这两字符串某一个字符出现次数相等,那么count +1
    flag = True
    while count< 26 and flag:
        if a1[count]==a2[count]:
            count=count+1
        else:
            flag=False
    return flag
print(sum2('aaaabbbbcccc','bbbbbccccaaaa'))

#排序和比较
def sum3(s1,s2):
    alist1=list(s1)
    alist2=list(s2)
    #排序   排序的时间复杂度
    alist1.sort()
    alist2.sort()
    flag=True
    pos=0
    while pos<len(s1) and flag:
        if alist1[pos]==alist2[pos]:
            pos=pos+1
        else:
            flag=False
    return flag
print(sum3('aaaaabbbbbcccc','bbbbbccccaaaaa'))
