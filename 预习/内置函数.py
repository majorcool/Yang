# 1. 用多行注释的方式，写出 Python 目前所有的内置函数
# https://docs.python.org/zh-cn/3/library/functions.html

# 2. 用多行注释的方式，说明什么是公共方法；同时，用一些代码举几个简单的例子
# 谁都能用的方法
"""
len()元素个数
del()删除元素
max()容器内最大
min()容器内最小
"""
# del------del(a)删除变量
a = [1, 2, 3]
del a[0]
print(a)
a = [1, 2, 3]
del a[0]
print(a)

# max + min---0 < a < A
b = "123456abcABC"
print(max(b))
print(min(b))
c = {1: "z", 2: "x"}
print(max(c))

# 大小---字典之间禁止比较大小
print(1 <= 2)
print("azzz" < "zaaa")
print([1, 2, 3] < [3, 2, 1])
print([9, 2, 3] < [3, 2, 9])
print([1, 999999999] < [2])
print((1, 2) < (2, 1))
print((1, 2) < (2,))  # 不加","报错

# 切片---字典禁止切片
print("zzzxz"[0:2])
print([1, "b", 1, 484][0:2])
print((1, "b", 1, 484)[-1::])

# 运算符---字典禁止*+
print([1, 2] * 2)
print((1, 2) * 2)
print([1] + [2])
print((1, 2) + (3, 4))

# in和not in
print("a" in "abc")
print("1" not in "123")
print([1] not in [1, 2, 3])
print(1 in [1, 2])
print("a" in {"a": "ads"})
print("ads" in {"a": "ads"})

# 完整for循环
# for 变量 in 集合
#    循环代码
# else:
#    没有通过break退出循环，就会执行的代码
for num in range(1, 4):
    print(num)
    # if num == 2:
    #     break
else:
    print("会执行吗")
print("循环结束")

students = {"name": "abc", "name1": "def"}
find_name = "abc"
for key in students:
    if students[key] == find_name:
        print("找到了%s" % find_name)
        break
else:
    print("抱歉没有找到%s" % find_name)
print("循环结束")

# 3. 用多行注释的方式，简单描述公共方法和内置函数的关系
# 公共方法属于内置函数，但是内置函数不一定是公共方法
# 1. 用多行注释的方式，写出 Python 目前所有的内置函数
# https://docs.python.org/zh-cn/3/library/functions.html

# 2. 用多行注释的方式，说明什么是公共方法；同时，用一些代码举几个简单的例子
# 谁都能用的方法
"""
len()元素个数
del()删除元素
max()容器内最大
min()容器内最小
"""
# del------del(a)删除变量
a = [1, 2, 3]
del a[0]
print(a)
a = [1, 2, 3]
del a[0]
print(a)

# max + min---0 < a < A
b = "123456abcABC"
print(max(b))
print(min(b))
c = {1: "z", 2: "x"}
print(max(c))

# 大小---字典之间禁止比较大小
print(1 <= 2)
print("azzz" < "zaaa")
print([1, 2, 3] < [3, 2, 1])
print([9, 2, 3] < [3, 2, 9])
print([1, 999999999] < [2])
print((1, 2) < (2, 1))
print((1, 2) < (2,))  # 不加","报错

# 切片---字典禁止切片
print("zzzxz"[0:2])
print([1, "b", 1, 484][0:2])
