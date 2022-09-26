# 4.2.5 参考上节课练习 #3.3.2 的打印菱形，定义一个函数，能够根据不同的参数打印不同大小的菱形
b=0
def aaa(n):
    n=int(n)
    if n%2!=0:
        a=(n+1)/2
        a=int(a)
        for b in range(1,a+1):
            print(" "*(a-b),end="")
            print("*" * (2 * b - 1))
        c=a-1
        for d in range(1,c+1):
            print(" "*d,end="")
            print("*" * (n-2*d))
aaa("7")