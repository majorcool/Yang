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

    def increase(self, livepeople):
        self.live = len(livepeople)

    def out(self, livepeople, rule):
        list1 = []
        count = 0
        output = 0
        for i in livepeople:
            list1.append(random.randint(0, rule.live-1))
        list1 = sorted(list1, reverse=True)
        for i in list1:
            repeat = 0
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
        x = random.randint(0, rule.live-1)
        return x


class Mafia(People):
    def kill(self, rule):
        x = random.randint(0, rule.live-1)
        return x


def game():
    livepeople = []
    ticket = []
    kill_person = 0
    old_counts = 0
    rule = Rule()
    goodpeople = []
    killer = []

    for i in range(0, 3):
        killer.append(Mafia())
    for i in range(0, 6):
        goodpeople.append(People())

    # for l in range(0, 3):
    #     livepeople.append(killer[l])

    livepeople = goodpeople + killer
    for i in killer:
        ticket.append(i.kill(rule))
    ticket = sorted(ticket, reverse=True)
    for q in ticket:
        new_counts = 0
        for w in ticket:
            if w == q:
                new_counts = new_counts + 1
        if new_counts >= old_counts:
            old_counts = new_counts
            kill_person = int(q)
    print(livepeople)
    print(goodpeople)
    print(killer)

    while len(goodpeople) > 0 and len(killer) > 0:
        if livepeople[kill_person] in goodpeople:
            print(livepeople[kill_person])
            goodpeople.remove(livepeople[kill_person])
        if livepeople[kill_person] in killer:
            killer.pop(kill_person- 6)
        livepeople.pop(kill_person)
        rule.increase(livepeople)
        print(len(livepeople))
        print(len(goodpeople))
        print(len(killer))
        print("kill")

        voted_people = rule.out(livepeople, rule)
        if livepeople[voted_people] in goodpeople:
            print(livepeople[voted_people])
            goodpeople.remove(livepeople[voted_people])
        if livepeople[voted_people] in killer:
            killer.pop(kill_person - 6)
        rule.increase(livepeople)
        print(len(livepeople))
        print(len(goodpeople))
        print(len(killer))
        print("vote")

    rule.victory(goodpeople)

game()

