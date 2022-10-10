# 5.3.6 编写一个函数 compare_dict(dict1, dict2)，判断两个字典中存在多少个完全相同的键值对，
# 将重复键值对的数量和重复的键值对保存在一个元祖中，将这个元祖作为返回值
def compare (dict1,dict2):
    list2=[]
    n=0
    a=0
    list1=[]
    dict1.update(dict2)
    for item in dict1.items():
        list1.append(item)
        list1=sorted(list1)
    while n<len(list1):
        if list1[n]==list1[n-1]:
            b=b+1
            list2.append(list1[n])
            list1.pop(list1[n])
            n=n-1
        n=n+1
    #list2.append(b)
    print(list2)
compare({"a":1,"b":2},{"a":1,"b":3})
