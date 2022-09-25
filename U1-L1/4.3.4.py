# 4.3.4 改写 #4.2.4：函数内不打印消息，如果输入的城市和国家匹配，将返回值设置为 'YES'；
# 如果不匹配，将返回值设置为 'NO'。调用 3 次函数，传入不同的参数，输出不同的结果。并且，使用 2 种调用的方式
def describe_city(a,b):
    if a=="shanghai" and b=="China":
        return "yes"
    if a=="sichuan" and b=="China":
        return "yes"
    if a=="niuyue" and b=="China":
        return "no"
a=describe_city("shanghai","China")
print(a)
print(describe_city("sichuan","China"))
print(describe_city("niuyue","China"))