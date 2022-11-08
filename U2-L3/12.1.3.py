"""下方代码中，有几个实例属性？几个实例方法？几个私有实例属性？几个私有实例方法？
class Fruit:
    def __init__(self):
        self.name = 'good'
        self._price = '100'
        self.__real_name = 'bad'
        self.__real_price = '1'

    def __del__(self):
        pass

    def __rot(self):
        print('no')

    def rot(self):
        print('yes')

    def _secret(self):
        print(self.__real_name)

    def __another_secret(self):
        print(self.__real_name)"""
#实例属性：2
#实例方法：2
#私有实例属性：2
#私有实例方法：2