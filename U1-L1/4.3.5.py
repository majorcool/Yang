# 4.3.5 改写 #4.2.5：函数内不打印菱形，将需要打印的菱形作为函数的返回值，用 2 种方式调用函数，传入不同的参数，打印 2 个不同的菱形
def aaa(n=2):
    n=int(n)
    a = 0
    b = " "
    c = 0
    d = 0
    if n != 0:
        if n >= 2:
            if n % 2 != 0:
                a = (n - 1) / 2
                d = 1
            elif n % 2 == 0:
                a = (n - 2) / 2
                d = 2
        # elif n==1:
        # print("*")
        elif n == 0:
            return""
        a = int(a)
        b = a
        for a in range(a, -1, -1):
            return " " * a
            c = (b - a) * 2 + 1
            return "*" * c
        a = b
        if d == 1:
            for a in range(1, a + 1):
                return " " * a
                c = (b - a) * 2 + 1
                return "*" * c
        if d == 2:
            return "*" * (n - 1)
            for a in range(1, a + 1):
                return " " * a
                c = (b - a) * 2 + 1
                return "*" * c
print(aaa(8))