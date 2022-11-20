  # 定义一个函数，参数为一个长度为 2n 的列表，其中包含 n+1 个不同的元素，只有 1 个元素重复了 n 次；返回重复了 n 次的元素
def element(n:list):
    for i in range(0,len(n)-1):
        for q in range(i + 1,len(n)-1):
            if n[i] == n[q]:
                return n[i]
print(element([1,2,2,2,3,4,2,2]))