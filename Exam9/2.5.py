# 2.5  Minimum Amount of Time to Fill Cups
# You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.
# You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively.
# Return the minimum number of seconds needed to fill up all the cups.
def fill_cups(amount: list[int]):
    amount = sorted(amount, reverse=True)
    second = 0
    while amount[0] != 0 and amount[1] != 0:
        amount = sorted(amount, reverse=True)
        amount[0] = amount[0] - 1
        amount[1] = amount[1] - 1
        second += 1
    amount = sorted(amount, reverse=True)
    second += amount[0]
    return second


print(fill_cups([5,4,4]))
