# 5.3.2 按要求操作下方的字典
# ① 循环遍历所有的 key
# ② 循环遍历所有的 value
# ③ 循环遍历出所有的 key 和 value
dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for key in dict1:
    print(key)
for value in dict1.values():
    print(value)
for item in dict1.items():
    print(item)