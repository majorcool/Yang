# 21.1.6  大小写转换
# 打开一个英文文本文件，将其中大写字母变成小写，小写字母变成大写
file = open('L12test.py', mode='r+', encoding='utf-8')
file1 = open('21.1.6output.py', mode='r+', encoding='utf-8')
upper = 'ABCDEFGHIZKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
tranform = file.readlines()
output = ''
print(tranform)
for i in tranform[0]:
    if i.isupper():
        output += lower[upper.find(i)]
    elif i.islower():
        output += upper[lower.find(i)]
    else:
        output += i
file1.writelines(output)
print(output)
file.close()
file1.close()
