# 1. 在 Version 3 的基础上，新建规则类 Rule
#   - 实例属性 rounds，记录游戏回合数
#   - 实例方法 judge()，游戏结束时，根据庄家的奖励，修改玩家的得分
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
            return [0, n-1]
        elif n == self.num:
            print("猜对了")
            self.again=True
        else:
            print("猜小了")
            return [1, n+1]

    def award(self, rounds:int):
        return 10 - rounds


class Player:
    def __init__(self):
        self.point = 0

    def guess_number(self, n1, n2):
        num1 = random.randint(n1, n2)
        print(num1)
        return num1


class Rule:
    def __init__(self):
        self.rounds = 0

    def add(self):
        self.rounds += 1

    def judge(self, zj, player):
        player.point = zj.award(self.rounds)

def game():
    first = 0
    second = 100
    zj = Dealer()
    wj = Player()
    rule = Rule()
    zj.set_number()
    print(zj.num)
    while zj.again == False:
        choice = zj.hint(wj.guess_number(first, second))
        if zj.again == True:
            break
        elif choice[0] == 0:
            second = choice[1]
        elif choice[0] == 1:
            first = choice[1]
        rule.add()
    rule.judge(zj, wj)
    print()
    print(wj.point)
    print("points:{}".format(zj.award(rule.rounds)))

game()