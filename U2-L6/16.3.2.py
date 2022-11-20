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