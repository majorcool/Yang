# 3.1.4 猜数游戏 v2.0
# 在程序中设定一个 1-100 的数
# 让用户输入一个数，最多有 5 次机会
# 如果用户猜对了，打印消息通知
# 如果用户猜错了，显示 “猜大了” 或 “猜小了”
import random
n = random.randint(1,100)
a=0
b=0
while b<5 :
    a = int(input("请输入数字:"))
    b=b+1
    if a > n :
        print("猜大了")
    elif a < n :
        print("猜小了")
    elif a == n:
        print("猜对了")
        break
