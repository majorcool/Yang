# 1. 定义玩家类 Player，包含属性 points；方法 punch()，随机返回 '10'，'5'，'2'（石头、布、剪刀）
# 2. 定义电脑类 Computer，继承自 Player
# 3. 定义函数 game()：玩家和电脑分别出拳（1 次），胜利方得 1 分；打印并返回结果
import os
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

class Computer(Player):
    pass


def game():
    player = Player()
    computer = Computer()
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

print(game())

