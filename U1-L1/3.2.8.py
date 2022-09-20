# 3.1.8 分别计算 1 到 100 中所有奇数、偶数的和
sj=0
so=0
for i in range(1,100,2):
    sj = sj+ i
for k in range(2,101,2):
    so = so +k
print(sj)
print(so)