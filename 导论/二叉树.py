class Child:
    def __init__(self):
        pass

    def input(self, n):
        if n > 12:
            return 1
        if n < 12:
            return 0
        if n == 0:
            return '[0]'


class LeftChild(Child):
    layer = {1: [5, 5], 2: [3, 5]}

    def add(self, count):
        counts = 1
        while 1:
            if count in LeftChild.layer:
                if count < LeftChild.layer[count][0]:
                    counts += 1
                elif count == LeftChild.layer[count][0]:
                    return '[0]' * count
                else:
                    return '[0]' * count + '[1]'


class RightChild(Child):
    layer = {1: [5, 15], 2: [3, 16]}

    def add(self, count):
        counts = 1
        while 1:
            if count in RightChild.layer:
                if count > RightChild.layer[count][1]:
                    counts += 1
                elif count == RightChild.layer[count][1]:
                    return '[1]' * count
                else:
                    return '[1]' * count + '[0]'


def test(n):
    child = Child()
    left = LeftChild()
    right = RightChild()
    choose = child.input(n)
    if choose == 0:
        print(left.add(n))
    elif choose == 1:
        print(right.add(n))
    else:
        print(choose)


test(12)