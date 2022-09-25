# 2.1.4 猜数游戏
import random#调用random
n = random.randint(1,100)
num = int(input("请输入数字："))
if num == n :
    print("猜对了")
elif num>n :
    print("猜大了")
else :
    print("猜小了")