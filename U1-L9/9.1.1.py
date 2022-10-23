# 递归阶乘
def factorial1(num):
    if num == 1:
        return 1
    else:
        return num * factorial1(num-1)
print(factorial1(5))