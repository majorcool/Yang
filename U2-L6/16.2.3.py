# 1. 在  Version 2 的基础上，修改玩家类的实例方法
#   - 添加两个参数 n1、n2，返回 n1-n2 之间的随机整数（包含 n1, n2）
#   - 根据庄家的提示，每次猜数时修改 n1 和 n2，以提高成功率
# 2. 按照 Version 1 修改主程序，只运行一次 game()
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


def game():
    first = 0
    second = 100
    count = 0
    zj = Dealer()
    wj = Player()
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
        count += 1
    print("points:{}".format(zj.award(count)))


game()
