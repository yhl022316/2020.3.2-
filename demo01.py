import time
'''
问题描述:使用函数,求前n个数的和
'''
def sum(n):
    start_time=time.time()
    sum=0
    for i in range(1,n+1):
        sum = sum + i
    end_time=time.time()
    return sum,end_time-start_time

print("计算机的结果是%d,需要%10.7f秒"%sum(1000000))

#高斯函数
def sum01(n):
    return (n*(n+1))/2
start_time=time.time()
print(sum01(1000000))
end_time=time.time()
print(end_time-start_time)