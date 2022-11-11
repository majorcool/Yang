#  15.1.2  大鱼吃小鱼 [50pts]
#  假设鱼塘的范围为 (x, y)，0 <= x, y <= 10；游戏开始时，在随机位置生成 1 只大鱼和 10 只小鱼
#  大鱼和小鱼随机上下左右移动，每一次移动，大鱼在每个方向分别最多移动 1 个单位， 小鱼最多移动 1 个单位；当移动到鱼塘边缘时，自动向反方向移动
#  大鱼的体力值为 100，每移动 1 个单位，就消耗 1 点体力；小鱼没有体力值；一次移动结束后，如果大鱼和小鱼相遇，大鱼会吃掉小鱼，体力恢复 20（最多恢复到 100）
#  当大鱼体力为 0，或小鱼的数量为 0 时，游戏结束
import random


class Fish:
    def __init__(self):
        self.X = random.randint(0, 10)
        self.Y = random.randint(0, 10)
        self.speed = 1

    def judge(self, a):
        if a < 0:
            a = a + 2
        if a > 10:
            a = a - 2
        return a

    def move(self):
        choose = random.randint(0, 1)
        if choose == 0:
            self.X = self.X + random.randint(-1, 1)
            self.X = self.judge(self.X)
        else:
            self.Y = self.Y + random.randint(-1, 1)
            self.Y = self.judge(self.Y)


class BigFish(Fish):
    def __init__(self):
        super().__init__()
        self.hp = 100

    def move(self):
        self.X = self.X + random.randint(-1, 1)
        self.X = self.judge(self.X)
        self.Y = self.Y + random.randint(-1, 1)
        self.Y = self.judge(self.Y)
        self.hp = self.hp - 1

    def eat(self):
        self.hp = self.hp + 20
        if self.hp > 100:
            self.hp = 100


class SmallFish(Fish):
    pass


big_fish = BigFish()
small_fish = []
eaten_fish = []
for i in range(10):
    small_fish.append(SmallFish())
while big_fish.hp > 0 and len(eaten_fish) < 10:
    big_fish.move()
    for s in small_fish:
        s.move()
        if (big_fish.X, big_fish.Y) == (s.X, s.Y):
            big_fish.eat()
            eaten_fish.append(s)
            del s
    if big_fish.hp == 0:
        print("big fish died")
    if len(eaten_fish) >= 10:
        print("all small fish are died")
print(big_fish.hp)
print(len(eaten_fish))

