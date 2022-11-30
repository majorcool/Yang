# 21.1.5  加密文件
# 打开一个英文的文本文件，将该文件中的每个字母加密后写入到一个新文件
# 加密的方法是：A ➝ B …… Z ➝ A（向后错位）；a ➝ z …… z ➝ y（向前错位）
# 除了大小写字母外，其他字符无变化
file = open('L12test.py', mode='r+', encoding='utf-8')
file1 = open('21.1.5output.py', mode='r+', encoding='utf-8')
upper = 'ABCDEFGHIZKLMNOPQRSTUVWXYZ'
upper_change = 'BCDEFGHIZKLMNOPQRSTUVWXYZA'
lower = 'abcdefghijklmnopqrstuvwxyz'
lower_change = 'zabcdefghijklmnopqrstuvwxy'
transform = file.readlines()
output = ''
for i in transform[0]:
    if i.isupper():
        output += upper_change[upper.find(i)]
    elif i.islower():
        output += lower_change[lower.find(i)]
    else:
        output += i
file1.writelines(output)
file.close()
file1.close()
