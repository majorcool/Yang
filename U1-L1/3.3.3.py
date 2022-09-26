# 3.3.3 按照下列格式打印九九乘法表
n=0
for a in range(1,10):
    if a>=1:
        print("\n")
        for b in range(1,a+1):
            n=a*b
            print(a,end="")
            print(" * ",end="")
            print(b,end=" = ")
            print(n,end="  ")


