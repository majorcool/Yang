# 5.3.5 编写一个函数 update_dict(dict_sample)，功能如下
# 用户输入一个 key-value（分 2 次输入），value 为数字类型，key 为 str 类型
# 如果原有的 dict_sample 中没有用户输入的 key，就添加这个 key-value
# 如果原有的 dict_sample 中存在用户输入的 key，保留较大的 value
# 将修改后的字典作为返回值
update_dict={"a":1,"b":2}
key1=str(input("key:"))
value=int(input("value:"))
if key1 in update_dict:
    if update_dict[key1]<value:
        update_dict[key1]=value
else:
    update_dict[key1]=value
print(update_dict)