# 6.1.4 定义一个函数，参数为 2 个字符串，从第 1 个字符串中删除第 2 个字符串中所有的字符，返回新的字符串
num1=input("num1")
num2=input("num2")
len1=len(num1)
for n in range(0,len1):
    a=num1[n]
    a=a.lstrip(num2)
    print(a,end="")