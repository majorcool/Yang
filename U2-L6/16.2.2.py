  # 在  Version 1 的基础上，修改主程序
  # - 不断进行游戏 game()
  # - 玩家得分小于 -10 时，结束程序
import random


class Dealer:
    def __init__(self):
        self.num = 0
        self.again = False

    def set_number(self):
        self.num = random.randint(0, 100)
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
        num1 = random.randint(0, 100)
        #print(num1)
        return num1


def game(zj, wj):
    zj.again = False
    count = 0
    zj.set_number()
    #print(zj.num)
    while zj.again == False:
        zj.hint(wj.guess_number())
        count += 1
    swardprint = int(zj.award(count))
    print(swardprint)
    # if not zj.award(count)  < -10:
    return swardprint

zj = Dealer()
wj = Player()
while game(zj,wj) >= -10:
    print("-------------")
