#定义一个函数 max_sec_average(l, n)，参数为纯数字列表 l 和正整数 n，返回 l 中连续 n 个数的最大平均值
def max_sec_average(l: list, n):
    sumz=0
    for a in range(0,len(l)):
        sum=0
        l.append(l[0])
        l.pop(0)
        for b in range(0,n):
            sum=sum+int(l[b])
        if sum>sumz:
            sumz=sum
    return sumz/n
print(max_sec_average([1,2,3,4,-5],2))


