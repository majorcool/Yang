class Animal:
    list1 = []

    def __init__(self, health, name):
        self.health = health
        self.name = name
        self.list1.append(self.name)

    def increase(self, n):
        self.health = self.health + n
        print(self.health)


class Manager:
    def __init__(self, n):
        self.performance = n

    def feed(self ,n:Animal):
        Animal.increase(n, 20)

    def perform(self ,n:Animal):
        Animal.increase(n, -20)

    def __inspect(self, n):
        self.performance = n


class Keeper(Manager):
    def __init__(self, v:Animal, n):
        super(Keeper, self).__init__(Manager)
        self.health = n
        if v.health < 80:
            self.performance -= 20

    def feed(self, n:Animal):
        Animal.increase(n, 20)


class Trainer(Manager):
    def __init__(self, v:Animal, n):
        super(Trainer, self).__init__(Manager)
        self.health = n
        if v.health < 80:
            self.performance -= 20

    def perform(self ,n:Animal):
        Animal.increase(n, -20)

def everyday():
    dog = Animal(100, "dog")
    m = Manager(100)
    m.feed(dog)
    k = Keeper(dog, 90)
    k.feed(dog)
    t = Trainer(dog, 90)
    t.perform(dog)
everyday()