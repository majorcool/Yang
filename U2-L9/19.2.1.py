# 19.2.1  随机数
# 让用户输入 2 个整数 start 和 end，打印这两个整数之间（包含两端）的一个随机整数
# 考虑用户输入不是整数的情况，以及 start > end 的情况，抛出异常并处理
import os
import random


class StartError(Exception):
    pass


def range(start, end):
    if start > end:
        raise StartError
    return random.randint(start, end)


try:
    print(range(2, 1))

except StartError:
    print('AreaError')