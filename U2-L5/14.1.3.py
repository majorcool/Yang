#Point 类包含 2 个属性，分别为点的横坐标与纵坐标
#Segment 类包含 2 个私有属性，分别为两个端点的坐标
#Segment 类包含 get_len() 方法，可以获得直线的长度
import math


class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.__xy1 = Points(x1, y1)
        self.__xy2 = Points(x2, y2)

    def get_len(self):
        final = ((self.__xy1.x - self.__xy2.x) ** 2 + (self.__xy1.y - self.__xy2.y) ** 2)**0.5
        print(final)

a=Segment(2,5,8,9)
a.get_len()


