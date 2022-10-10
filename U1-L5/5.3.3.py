# 5.3.3 下方是一个字典，按要求完成操作
# ① 字典的长度是多少
# ② 请修改 'java' 这个 key 对应的 value 值为 98
# ③ 删除 c 这个 key
# ④ 增加一个 key-value 对，key 值为 php, value 是 90
# ⑤ 获取所有的 key 值，存储在列表里
# ⑥ 获取所有的 value 值，存储在列表里
# ⑦ 判断 javascript 是否在字典中
# ⑧ 获得字典里所有 value 的和
# ⑨ 获取字典里最大的 value
# ⑩ 获取字典里最小的 value
# ⑪ 字典 dic1 = {'php': 97}，将 dic1 的数据更新到 dic 中
dic = {
    'python': 95,
    'java': 99,
    'c': 100
}
print(len(dic))
dic["java"]=98
print(dic)
dic.pop("c")
print(dic)
dic["php"]=90
print(dic)
list1=[]
for key in dic:
    list1.append(key)
print(list1)
list2=[]
for value in dic.values():
    list2.append(value)
print(list2)
if "javascript" in dic:
    print(True)
else:
    print(False)
sum=0
for a in dic.values():
    sum=a+sum
print(sum)
max=0
for b in dic.values():
    if b>max:
        max=b
print(max)
small=999999999999999999999999999999999999
for c in dic.values():
    if small>c:
        small=b
print(small)
dic1 = {'php': 97}
dic.update(dic1)
print(dic)