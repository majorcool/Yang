# 在 17.1.1 的基础上添加一个逻辑：如果在主程序中删除了水果实例，就要修改对应的类属性 nums
# 下方为预期的运行效果
class Fruit:
    variety = 0


class Apple(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Apple.nums += 1

    def __del__(self):
        Apple.nums -= 1
        if Apple.nums == 0:
            Fruit.variety -= 1


class Banana(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Banana.nums += 1

    def __del__(self):
        Banana.nums -= 1
        if Banana.nums == 0:
            Fruit.variety -= 1


class Grape(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Grape.nums += 1

    def __del__(self):
        Grape.nums -= 1
        if Grape.nums == 0:
            Fruit.variety -= 1


class Melon(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Melon.nums += 1

    def __del__(self):
        Melon.nums -= 1
        if Melon.nums == 0:
            Fruit.variety -= 1


class Orange(Fruit):
    nums = 0
    Fruit.variety += 1

    def __init__(self):
        Orange.nums += 1

    def __del__(self):
        Orange.nums -= 1
        if Orange.nums == 0:
            Fruit.variety -= 1


a = Apple()
b = Banana()
c = Grape()
d = Melon()
e = Orange()
f = Orange()
del a
del c
del e
print(Apple.nums, Banana.nums, Grape.nums, Melon.nums, Orange.nums, Fruit.variety)