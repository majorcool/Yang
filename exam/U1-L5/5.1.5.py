# 5.1.5 定义一个函数，作用是将列表中的数字元素全部扩大两倍，其他类型保持不变，修改完成后，将新列表作为返回值
list = [5, 2, 3, 4, 5, 6, 7, 8, 9]
def nnn():
    z= len(list)
    for n in range(0,z):
        num = list[n] * 2
        list[n] = num
    return list
print(nnn())



