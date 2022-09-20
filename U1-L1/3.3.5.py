# 3.3.5 有 1 2 3 4 四个数字，组成互不相同且无重复数字的 3 位数，打印出所有结果
g=1
s=1
b=1
for b in range(1,5):
    print(b,end="")
    for s in range(1,5):
        print(s,end="")
        for g in range(1,5):
            print(g)
            break
        break
        #不会