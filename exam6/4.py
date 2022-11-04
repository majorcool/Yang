#定义一个函数 max_sec_average(l, n)，参数为纯数字列表 l 和正整数 n，返回 l 中连续 n 个数的最大平均值
def max_sec_average(l:str, n):
    sum=0
    l=sorted(l)[::-1]
    for a in range(0,n):
        sum=sum+int(l[a])
    print(sum/n)
max_sec_average("123456",2)


