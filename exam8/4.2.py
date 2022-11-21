# 定义一个函数，参数为一个只含整数的列表，判断列表所有元素的乘积的正负性
# 如果乘积大于零，返回 1；等于零，返回 0；小于零，返回 -1
def judge(n:list):
    count = 0
    n = sorted(n, reverse=False)
    if 0 in n:
        return 0
    for i in n:
        if i < 0:
            count += 1
    if count % 2 == 1:
        return -1
    return 1


print(judge([-1,1,-1,1,-1]))