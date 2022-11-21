# 1. 添加骗子类 Fraud，包含方法 lie()，随机返回 'lose'，'tie'
# 2. 为 Player 类添加方法 challenge()，随机返回 'yes'，'no'
# 3. 修改 game()：玩家和电脑出拳后，玩家需要询问骗子结果，如果玩家不挑战，
# 则按照骗子的结果进行计分；如果玩家挑战，则按照真实情况计分，但是分值 * 2
import random


class Player:
    def __init__(self):
        self.points = 0

    def punch(self):
        n = random.randint(1, 3)
        if n == 1:
            return '10'
        if n == 2:
            return '5'
        if n == 3:
            return '2'

    def challenge(self):
        rate = random.randint(1, 2)
        if rate == 1:
            return 'yes'
        else:
            return 'no'


class Computer(Player):
    pass

class Fraud:
    def __init__(self):
        pass

    def lie(self):
        rate = random.randint(1, 2)
        if rate == 1:
            return 'lose'
        else:
            return 'tie'

def game(player, computer):
    while 1:
        pl = player.punch()
        co = computer.punch()
        if pl == '2' and co == '10':
            computer.points += 1
            return 'computer win'
        elif pl == '10' and co == '2':
            player.points += 1
            return 'player win'
        if pl < co:
            player.points += 1
            return 'player win'
        elif co < pl:
            computer.points += 1
            return 'computer win'
        print('the same action,again')

def game2():
    fraud = Fraud()
    player = Player()
    computer = Computer()
    if player.challenge() == "no":
        print(fraud.lie())
    else:
        print(game(player, computer))
        player.points *= 2
        computer.points *= 2
        print(player.points)
        print(computer.points)



game2()
