"""已知左侧的输出为 30，右侧的输出为？
class Test1:
    def __init__(self):
        self.n1 = 10
        self.n2 = 10
        self.n3 = 10

    def test(self):
        pass


test = Test1()
print(len(dir(test)))
class Test1:
    def __init__(self):
        self._n1 = 10
        self.__n2 = 10
        self.___n3 = 10

    def ____test(self):
        pass


test = Test1()
print(len(dir(test)))"""
#输出：30