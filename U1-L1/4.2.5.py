# 4.2.5 参考上节课练习 #3.3.2 的打印菱形，定义一个函数，能够根据不同的参数打印不同大小的菱形
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
            print("")
        a = int(a)
        b = a
        for a in range(a, -1, -1):
            print(" " * a, end="")
            c = (b - a) * 2 + 1
            print("*" * c)
        a = b
        if d == 1:
            for a in range(1, a + 1):
                print(" " * a, end="")
                c = (b - a) * 2 + 1
                print("*" * c)
        if d == 2:
            print("*" * (n - 1))
            for a in range(1, a + 1):
                print(" " * a, end="")
                c = (b - a) * 2 + 1
                print("*" * c)
aaa("8")