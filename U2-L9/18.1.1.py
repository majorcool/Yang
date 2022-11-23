# 18.1.1  理解 '对象'
# 定义 A 类
# 属性
# - 类属性 nums
# - 实例属性 nums
# 方法
# - 静态方法 test1，打印 dir(A)，但是，不打印其中的内置方法
# - 类方法 test2，打印 dir(cls)，但是，不打印其中的内置方法
# - 实例方法 test(3)，打印 dir(self)，但是，不打印其中的内置方法
# 主程序
# 调用静态方法 test1()
# 调用类方法 test2()
# 调用实例方法 test(3)
class A:
    nums = 0

    @staticmethod
    def test1():
        print([name for name in dir(A) if name[:2:] != '__' and name[::-1][:2:] != '__'])

        l = []
        for i in dir(A):
            if i[:2:] != '__' and i[::-1][:2:] != '__':
                l.append(i)
        print(l)

    @classmethod
    def test2(cls):
        l = []
        for i in dir(cls):
            if i[:2:] != '__' and i[::-1][:2:] != '__':
                l.append(i)
        print(l)

    def __init__(self):
        self.num = 0

    def test3(self):
        l = []
        for i in dir(self):
            if i[:2:] != '__' and i[::-1][:2:] != '__':
                l.append(i)
        print(l)


def function():
    a = A()
    A.test1()
    A.test2()
    a.test3()


function()
a = [A() for _ in range(2)]
print(a)
