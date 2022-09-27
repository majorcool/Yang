# 4.3.6 改写 #4.2.6：函数内打印乘法表，同时，将打印的算式条数作为函数的返回值
# 例如完整的乘法表，应有 9+8+7+……+1 共 45 条算式。用任意的方式调用函数，打印乘法表的同时，在下方打印算式条数

def num(n):
    c = 0
    sum = 0
    for a in range(1,n+1):
        if a>=1:
            for b in range(1,a+1):
                s=a*b
                print(a,end="")
                print(" * ",end="")
                print(b,end=" = ")
                print(s,end="  ")
            print("")
            sum=sum+b
    return sum
nnn=num(8)
print(nnn)

