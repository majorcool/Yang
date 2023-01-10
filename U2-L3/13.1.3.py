"""下方代码中的 3 个实例 a，b，c，和 3 个实例方法 get_X()，get_Y()，get_Z()
分别说明 a，b，c 能调用哪些实例方法？"""


class A:
    def __init__(self):
        self.X = 1
        self.Y = 2
        self.Z = 3

    def get_X(self):
        print(self.X)


class B(A):
    def get_Y(self):
        print(self.Y)


class C(B):
    def get_Z(self):
        print(self.Z)


a = A()  # a能调用class A(get_X)的所有方法
b = B()  # b能调用class B(get_Y)和class A(get_X)的所有方法
c = C()  # c能调用class A(get_X)和class B(get_Y)和class C(get_Z)的所有方法