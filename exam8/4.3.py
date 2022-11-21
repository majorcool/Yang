# 汉明距离是一个概念，表示两个相同长度的字符串对应位置的不同字符的数量
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目
# 定义一个函数，参数为 2 个整数 x 和 y，计算并返回它们之间的汉明距离
def displacement(x :int, y :int):
    count = 0
    x = str(bin(x))[2::]
    y = str(bin(y))[2::]
    if len(x) > len(y):
        y = "0" * (len(x) - len(y)) + y
    if len(y) > len(x):
        x = "0" * (len(y) - len(x)) + x
    print(x, y)
    for i in range(0,len(x)):
        if not x[i] == y[i]:
            count += 1
    return count


print(displacement(3, 1))