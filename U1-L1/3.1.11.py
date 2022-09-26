# 3.1.11 制作一个动态的进度条（提示：使用 print 函数的 end 参数）
import time

a = 1

while a <= 5:

    print("*", end='')

    a += 1
    time.sleep(0.5)
