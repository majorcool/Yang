# 3.3.2 用户输入高度（行数），按照下方格式打印 1 个菱形
n=int(input("请输入行数:"))
a=0
b=" "
c=0
d=0
if n!=0:
    if n>=2:
        if n%2!=0:
            a=(n-1)/2
            d=1
        elif n%2==0:
            a=(n-2)/2
            d=2
    elif n==0:
        print("")
    a=int(a)
    b=a
    for a in range(a,-1,-1):
        print(" "*a,end="")
        c=(b-a)*2+1
        print("*"*c)
    a=b
    if d==1:
        for a in range(1,a+1):
            print(" "*a,end="")
            c=(b-a)*2+1
            print("*"*c)
    if d==2:
        print("*"*(n-1))
        for a in range(1,a+1):
            print(" "*a,end="")
            c=(b-a)*2+1
            print("*"*c)