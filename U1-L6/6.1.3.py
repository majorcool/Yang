# 6.1.3 定义一个函数，参数为 1 个字符串，对该字符串进行逆序，返回逆序后的字符串
num=input("str:")
len1=len(num)
for n in range(0,len1):
    a=num[-n-1]
    print(a,end="")