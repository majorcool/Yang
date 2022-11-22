class Child:
    def __init__(self):
        pass

    def input(self, n):
        if n > 12:
            return 1
        if n < 12:
            return 0
        if n == 12:
            return '[0]'


class LeftChild(Child):
    layer = {1: [5, 5], 2: [3, 5], 3: [-99999999999, 5]}

    def add(self, count):
        counts = 1
        while 1:
            if counts in LeftChild.layer:
                if count < LeftChild.layer[counts][0]:
                    counts += 1
                elif count == LeftChild.layer[counts][0]:
                    return '[0]' * counts
                else:
                    return '[0]' * counts


class RightChild(Child):
    layer = {1: [5, 15], 2: [5, 16], 3: [5, 99999999999999999999]}

    def add(self, count):
        counts = 1
        while 1:
            if counts in RightChild.layer:
                if count > RightChild.layer[counts][1]:
                    counts += 1
                elif count == RightChild.layer[counts][1]:
                    return '[1]' * counts
                else:
                    return '[1]' * counts


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


test(1)