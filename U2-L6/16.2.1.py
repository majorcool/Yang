# 16.2.1  猜数游戏 OOP Version 1
# 1. 定义庄家类 Dealer
#   - 实例方法 set_number()，返回一个 0-100 的随机整数
#   - 实例方法 hint(n)，根据 n 和设定数字的关系，打印 '猜大了'，'猜小了'，'猜对了'
#   - 实例方法 award(rounds)，根据回合数[1, 2, 3 ..., 20, ...] 返回奖励得分 [10, 9, 8, ..., -9, ...]
# 2. 定义玩家类 Player
#   - 实例属性 point，记录玩家的得分
#   - 实例方法 guess_number()，返回一个 0-100 的随机整数
# 3. 定义函数 game()
#   - 游戏开始时，庄家设定一个随机整数
#   - 每一回合，由玩家猜数，随后庄家进行判定
#   - 玩家猜对时，获取得分，游戏结束
# 4. 编写主程序
#   - 运行 1 次 game()
import random


class Dealer:
    def __init__(self):
        self.num = 0
        self.again = False

    def set_number(self):
        self.num = random.randint(0, 10)
        return self.num

    def hint(self, n):
        if n > self.num:
            print("猜大了")
        elif n == self.num:
            print("猜对了")
            self.again=True
        else:
            print("猜小了")

    def award(self, rounds:int):
        return 10 - rounds


class Player:
    def __init__(self):
        self.point = 0

    def guess_number(self):
        num1 = random.randint(0, 10)
        print(num1)
        return num1


def game():
    count = 0
    zj = Dealer()
    wj = Player()
    zj.set_number()
    print(zj.num)
    while zj.again == False:
        zj.hint(wj.guess_number())
        count += 1
    print(zj.award(count))

game()