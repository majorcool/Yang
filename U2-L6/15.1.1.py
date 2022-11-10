#15.1.1  判断下方代码的 MRO 顺序
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()
print(D.mro())