# 5.2.6 小明在黑板上写了一个整数数列，先将数列由小到大排好，每次擦去其中的第 1 个和第 2 个数，假设擦去数的值分别为 a 和 b，再在数列中添加一个数
# a * b + 1 并保持数列有序，如此下去，直至黑板上只剩下一个数，打印出这个数
first_list = [11,45,141,145,14,114514] # doge
num3 = 0
while len(first_list) > 0 and num3 < 5:
    num1 = first_list[0]
    num2 = first_list[1]
    del first_list[0]
    del first_list[0]
    first_list.append(num1 * num2 + 1)
    first_list.sort()
    num3 += 1
print(first_list[0])