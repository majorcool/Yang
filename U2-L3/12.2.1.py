#12.2.1  修改父类的稀有属性
#为 B 类增加一个实例方法，功能是修改 A 类中的私有属性 a 的值，不要使用 _A__a 进行修改
#你可能需要同时修改 A 类
class A:
    def __init__(self):
        self.__a = 1#__a=_A__a

    def change(self):#selfA中的a
        self.__a = 6
        return self.__a

class B(A):
    def change1(self):
        return self.change()#selfB中的a

a=B()
print(a.change1())