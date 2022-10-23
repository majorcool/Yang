#定义一个函数，参数为 2 个字符串 s1，s2，判断 s1 是否可以通过打乱顺序来得到 s2，如果可以返回 True，不可以返回 False
def diff(s1, s2):
    return sorted(s1) == sorted(s2)
print(diff("1asdfghjkl3", "lkjhgfdsa31"))