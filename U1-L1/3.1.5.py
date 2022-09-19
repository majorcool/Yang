# 3.1.5 猜数游戏 v2.1
# 在程序中设定一个 1-100 的数
# 让用户输入一个数，用户可以一直猜，直到猜对为止
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，告知误差范围：如果误差超过 50，打印 '离谱'；误差超过 30，打印 'nonono'；误差不超过 10，打印 'close!'
import random
n = random.randint(1,100)
a=0
while 1 :
    a = int(input("请输入数字:"))
    if a > n :
        if a - n > 50 :
            print("离谱")
        elif a-n>30 and a-n<=50 :
            print("nonono")
        elif a-n<=10 :
            print("close!")
        else :
            print("再猜")
    elif a < n :
        if n - a > 50:
            print("离谱")
        elif n - a > 30 and a - n <= 50:
            print("nonono")
        elif n - a <= 10:
            print("close!")
        else :
            print("再猜")
    elif a == n:
        print("猜对了")
        break