#将下方代码中的实例属性改为私有属性
#编写一个实例方法，功能是将私有属性重新赋值，但是要进行判断，新的值长度需要小于 10，否则保持不变
class Person:
    def __init__(self, name):
        self.__name = name

    def rename(self):
        while 1:
            new_name = input("new name:")
            if len(new_name) < 10:
                break
        self.__name=new_name
        return self.__name

a=Person("zqw")
print(a.rename())