class Animal:
    def __init__(self, health):
        self.health = health

    def increase(self, n):
        self.health = self.health + n
        return self.health


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
    def __init__(self, n:Animal, v):
        self.performance = v
        if n.health < 80:
            self.performance -= 20

class Trainer(Manager):
