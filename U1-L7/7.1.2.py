#定义一个函数，参数为一个正整数 n，判断 n 是不是 哈哈数
#哈哈数的定义如下：对于一个正整数，计算每一位数字的平方，求和，得到一个新的正整数
#对于新的正整数，重复这个过程，直到和变为 1，也可能是无限循环但始终不为 1。
#如果最终和为 1，那么这个数就是哈哈数，返回 True，否则返回 False
num=input("num")
while 1:
    num = " ".join(num)#不知为何错
    num = num.split(" ")
    sum = 0
    for n in range(0, len(num)):
        num2=int(num[n])
        num[n] = num2 * num2
        sum += num[n]
    print(num)
    if sum == 1:
        break