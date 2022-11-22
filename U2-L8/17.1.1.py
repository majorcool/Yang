# 定义水果类 Fruit，包含类属性品种 variety
# 定义 5 个品种的水果类，继承自 Fruit，包含类属性数量 nums
# 在主程序中分别为 5 种水果创建若干实例，打印水果的品种数以及各自品种的数量
class Fruit:
    variety = 0


class Apple(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Apple.nums += 1


class Banana(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Banana.nums += 1


class Grape(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Grape.nums += 1


class Melon(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Melon.nums += 1


class Orange(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Orange.nums += 1


a = Apple()
b = Banana()
c = Grape()
d = Melon()
e = Orange()
f = Orange()
print(Apple.nums, Banana.nums, Grape.nums, Melon.nums, Orange.nums, Fruit.variety)