#1. 分析下方代码的多态性
#2. 解释维基百科中描述的 '对象是一个鸭子' 是什么意思（本次作业的核心问题）
class Duck:
    def quack(self):
        print("这鸭子正在嘎嘎叫")

    def feathers(self):
        print("这鸭子拥有白色和灰色的羽毛")


class Person:
    def quack(self):
        print("这人正在模仿鸭子")

    def feathers(self):
        print("这人在地上拿起1根羽毛然后给其他人看")


def in_the_forest(duck):  # 这段代码传入了duck参数，并调用了两种类方法。Duck类和Person类都有quack,feathers方法，所以这个函数实现了
    # 不同类中的不同对象进行不同运算，展现了这个函数的多态性。对象是一只鸭子也就是指只要具有鸭子属性，方法的不同类的对象，都可进行这种对鸭子函数
    # 的运算。
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()