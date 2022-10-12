# 6.1.7 定义一个函数，参数为 1 个字符串和 1 个只包含字符串的列表，用字符串作为连接符，将列表的每个元素连接起来，返回连接后的字符串
# 例如，参数为 '123' 和 ['a', 'b', 'c']，返回 'a123b123c'
str1="1"
num=""
list1=["a","s","c","r","g","j","k","l"]
for n in list1:
    num=num+n
output=str1.join(num)
print(output)
print(str1.join(list1))