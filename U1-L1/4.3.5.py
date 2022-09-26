# 4.3.5 改写 #4.2.5：函数内不打印菱形，将需要打印的菱形作为函数的返回值，用 2 种方式调用函数，传入不同的参数，打印 2 个不同的菱形
a=0(不知问题所在)
b=0
r=0
z=0
def nnn(n):
    n = int(n)
    if n % 2 != 0:
        a = (n + 1) / 2
        a = int(a)
        for b in range(1, a + 1):
            r= (r+"\n")+(" " * (a - b) + "*" * (2 * b - 1))
        c = a - 1
        for d in range(1, c + 1):
            z=(z+"\n")+( " " * d + "*" * (n-2 * d))
        return r+"\n"+z
x=nnn(7)
print(x)