# 6.1.2 定义一个函数，参数为 1 个字符串，判断它是否为 '回文数'
# 如果一个数字左右对称，就是 '回文数'，如 123454321, 1221
num=input("num:")
n=0
x=1
while n!=1:
    for a in range(0,9):
        z=len(num)
        if z<=1:
            print("是回文")
            n=1
            break
        else:
            if num.find(x-1)==num.find(-x):
                num = num.strip(a)
                break
            else:
                print("不是回文")
                n=1
                break