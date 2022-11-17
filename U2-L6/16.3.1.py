# 根据游戏描述，使用面向对象的方式完成游戏程序的设计（无需输入，展示游戏过程即可）
# 1. 游戏人数为 10 人，包括 1 名法官，3 名 Mafia，6 名好人
# 2. 游戏开始时，法官让所有人闭眼，然后所有 Mafia 睁开眼睛，决定 1 个受害者（退出游戏）
#   每个 Mafia 指定一个号码，选择票数最多的号码
#   如果所有号码的票数一样多，就选择号码最大的
# 3. 大家睁眼，讨论谁是 Mafia，讨论后选出一人并处决（退出游戏）
#   每个玩家（包括 Mafia 和好人）指定一个号码，选择票数最多的号码（要求体现多态性）
#   如果所有号码的票数一样多，就选择号码最大的
# 4. 重复步骤 2~3，如果所有的好人被处决，Mafia 获胜；如果找出所有的 Mafia，好人获胜
import random

class Rule:
    def __init__(self):
        self.live = 9

    def increase(self, num):
        self.live += num

    def killpeople(self, x1=-3, x2=-2, x3=-1):
        if x1 == x2:
            return x1
        elif x2 == x3:
            return x2
        elif x1 == x3:
            return x1
        else:
            kill = sorted([x1, x2, x3], reverse=True)
            kill = list(set(kill))
            return kill[0]

    def out(self, len, people):
        list1 = []
        repeat = 0
        count = 0
        output = 0
        for i in range(0, len):
            list1.append(people.vote(self))
        list1 = sorted(list1, reverse=True)
        for i in list1:
            for z in list1:
                if i == z:
                    repeat += 1
            if repeat >= count:
                output = i
        return output

    def victory(self, goodpeople):
        if len(goodpeople) < 0:
            print("killer win")
        else:
            print("good people win")
class People:
    def __init__(self):
        self.life = True

    def vote(self, rule):
        x = random.randint(0, rule.live)
        return x


class Mafia(People):
    def kill(self, rule):
        x = random.randint(0, rule.live)
        return x


def game():
    livepeople = []
    killer = []
    rule = Rule()
    goodpeople = []
    oldchoice = -1
    for i in range(0, 9):
        livepeople.append(People())
    for i in range(0, 3):
        while 1:
            newchoice = random.randint(0, 9)
            if not oldchoice == newchoice:
                break
        print(livepeople)
        livepeople[newchoice] = Mafia()
        killer.append(livepeople[newchoice])
    for i in livepeople:
        if not i in killer:
            goodpeople.append(i)
    while len(goodpeople) > 0 and len(killer) > 0:
        if len(killer) == 3:
            died = rule.killpeople(killer[0].kill(rule), killer[1].kill(rule), killer[2].kill(rule))
        if len(killer) == 2:
            died = rule.killpeople(killer[0].kill(rule), killer[1].kill(rule))
        else:
            died = rule.killpeople(killer[0].kill(rule))
        if livepeople[died] in goodpeople:
            goodpeople.remove(livepeople[died])
        if livepeople[died] in killer:
            killer.remove(livepeople[died])
        livepeople.pop(died)
        rule.increase(-1)
        rule.out(len(livepeople), goodpeople[0])
        rule.increase(-1)
    rule.victory(goodpeople)


game()
