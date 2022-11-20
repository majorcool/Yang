# 定义一个函数，参数为一个长度为 2n 的列表 [x1,x2,...,xn,y1,y2,...,yn]
# 调整顺序为 [x1,y1,x2,y2,...,xn,yn]，并返回调整后的列表
def order(n:list):
    new_list = []
    for i in range(0, int(len(n)/2)):
        new_list.append(n[i])
        new_list.append(n[i + int(len(n)/2)])
    return new_list
print(order([1,4,2,3,3,2,4,1]))