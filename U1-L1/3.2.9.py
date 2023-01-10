# 3.1.9 质数判断：用户输入一个正整数，用程序判断是否为质数
b=0
n=int(input("请输入数:"))
if n>2:
    for a in range(2,n):
        if n%a==0 and n!=2:
            print("非质数")
            b=1
            break
if b==0 and n!=1:
    print("质数")
"""elif n==1:
    print("非质数")
elif n==2:
    print("质数")"""
if n==1:
    print("非质数")

