#12.2.1  修改父类的稀有属性
#为 B 类增加一个实例方法，功能是修改 A 类中的私有属性 a 的值，不要使用 _A__a 进行修改
#你可能需要同时修改 A 类
class A:
    def __init__(self):
        self.__a = 1

    def change(self):
        self.__a = 2
        return self.__a

class B(A):
    pass

a=A()
print(a.change())