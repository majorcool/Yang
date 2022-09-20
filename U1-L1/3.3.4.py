# 3.3.4 用户输入 1 个整数，打印出这个整数的所有因数。打印后程序持续运行，而非结束
while 1:
    n=int(input("请输入整数:"))
    print(n,end="的因数有:")
    for a in range(1,n+1):
        if n%a==0:
            print(a,end=" ")
    print("")
