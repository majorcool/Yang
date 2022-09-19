# 3.1.9 质数判断：用户输入一个正整数，用程序判断是否为质数
a=int(input("请输入数:"))
n=1
while n != a:
    n=n+1
    if a % n == 0 and n!=a:
        print("非质数")
        break
if n == a:
    print("质数")

