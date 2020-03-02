import time
'''
问题描述:使用函数,求前n个数的和
'''
def sum(n):
    start_time=time.time()
    sum=0
    for i in range(1,n+1):#n+1表示  往后进一位可以遍历到n   (1,n+1)的意思是从1遍历到1000000.
        sum = sum + i#当i=1时   sum=0+1=1  sum=1   当i=2时  sum=1+2=3
    end_time=time.time()
    return sum,end_time-start_time

print("计算机的结果是%d,需要%10.7f秒"%sum(1000000))#1000000表示的是def sum(n)的值

#高斯函数
def sum01(n):
    return (n*(n+1))/2
start_time=time.time()
print(sum01(1000000))
end_time=time.time()
print(end_time-start_time)


a=[1,2,3,4,5,6,7,8,9]
for i in a:
    print(i)

a=0
for i in range(101):
    a=a+i
    print(a)


a=[1,1,1,1,1,1,1]
for i in range(len(a)):
    print(i)