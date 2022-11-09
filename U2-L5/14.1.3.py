#Point 类包含 2 个属性，分别为点的横坐标与纵坐标
#Segment 类包含 2 个私有属性，分别为两个端点的坐标
#Segment 类包含 get_len() 方法，可以获得直线的长度
import math


class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, xy1, xy2):
        self.__xy1 = str(xy1).split(',')
        self.__xy2 = str(xy2).split(',')

    def get_len(self):
        final = math.sqrt(
            (((int(self.__xy1[0])) - int(self.__xy2[0]))) ** 2 + (((int(self.__xy1[1])) - int(self.__xy2[1]))) ** 2)
        print(final)

a=Segment('2,5','8,9')
a.get_len()


