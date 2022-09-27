# 4.3.5 改写 #4.2.5：函数内不打印菱形，将需要打印的菱形作为函数的返回值，用 2 种方式调用函数，传入不同的参数，打印 2 个不同的菱形

def nnn(n):
    a = 0  #
    b = 0
    r = ""
    z = ""
    n = int(n)
    if n % 2 != 0:
        a = (n + 1) / 2
        a = int(a)
        for b in range(1, a + 1):
            r = (r+"\n")+(" " * (a - b) + "*" * (2 * b - 1))
        c = a - 1
        for d in range(1, c + 1):
            z = (z+"\n")+( " " * d + "*" * (n-2 * d))
        return r+z
    else:
        return False
x=nnn(7)
print(x)