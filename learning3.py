class List:
    def __init__(self):
        self.order = []

    def add(self, n):
        self.order.append(n)

    def delate(self):
        self.order.pop(0)

    def isempty(self):
        if len(self.order) == 0:
            return True
        else:
            return False

    def popmethod(self):
        self.order.pop()

    def max(self):
        o = -9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        for i in self.order:
            if i > o:
                o = i
        return o

    def mini(self):
        o = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        for i in self.order:
            if i < o:
                o = i
        return o

    def first(self):
        print(self.order[0])

    def lenth(self):
        return len(self.order)