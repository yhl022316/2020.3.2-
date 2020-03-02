"""
乱序字符串是指一个字符串指示另一个字符串重新排列
前提:字符串是26个小写字符集合组成  长度相同
比如: Python   onthpy
目的:
写一个布尔函数(返回布尔值的函数)

"""
def ang(s1,s2):
    if len(s1)!=len(s2):
        return False
a=ang('hjkjlkjl','huhkjkjjlkjlkj')
print(a)

# 乱序字符串是指一个字符串只是另一字符串的重新排列
# 前提：字符串由26个小写字母集合组成，长度相同
# 比如：python
# typhon
# head
# deah
# 目的：
# 写一个布尔函数（返回值是布尔值的函数）
# solutions1('abcd', 'dbca')


#穷举法:排除
# def sum1(s1,s2):
#     flag=
#     while
