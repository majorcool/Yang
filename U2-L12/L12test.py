# 21.1.1  文件指针位置
# 使用 open() 函数打开文件并读取文件中的内容时，总是会从文件的第一个字符（字节）开始读起。那么，有没有办法可以指定读取的起始位置呢？
# 借助搜索引擎查询解决方案，配合代码体现成果
file = open('L12test.py', encoding='utf-8', mode='r+')
file.seek(2)
print(file.readlines())
file.close()
# 21.1.2  文件对象的属性和方法
# Python 一切皆对象，那么文件对象有哪些属性和方法呢？
# 借助搜索引擎查询解决方案，配合代码体现成果
'''open write writelines read readline readlines seek'''
# 读取一个文件,显示除了以 # 号开头的行以外的所有行
# 需要注意的是，其中一些行的 # 后存在空格，在打印时需要删除
file = open('L12test.py', mode='r+', encoding='utf-8')
count = -1
content = 'x'
while content != '':
    content = file.readline()
    count += 1
file.close()
file2 = open('L12test.py', mode='r+', encoding='utf-8')
for i in range(count):
    content = file2.readline()
    content1 = content[:1:]
    if content1 == '#':
        content = content[1::]
        if content[0] == ' ':
            while content[0] == ' ':
                content = content[1::]
                print(content.strip())
        else:
            print(content.strip())
file2.close()
# 21.1.4  读取数字
# 已知文本文件中存放了若干数字，请编写程序读取所有数字（0-10），排序以后进行输出
# 需要注意的是，数字中如果出现了 10，则读取为 10，如果 0 的前面不为 1，则为 0
file = open('L12test.py', mode='r+', encoding='utf-8')
storage = file.readlines()
list1 = []
for i in range(0, len(storage[0])):
    if storage[0][i] == '1' and storage[0][i+1] == '0':
        list1.append(10)
        continue
    list1.append(int(storage[0][i]))
print(sorted(list1, reverse=True))
file.close()
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
# 语文老师布置了一篇作文，学生提交的文件名各不相同，但是文件的第一行均为学生的姓名
# 借助刚学过的文件操作，编写一个可以批量修改文件名的小程序
change = input('change:')
file = open('L12test.py', mode='r+', encoding='utf-8')
student_essay = ['L12test.py']
for i in range(len(student_essay)):
    file = open(student_essay[i], mode='r+', encoding='utf-8')
    file.readline()
    content = ''.join(file.readlines())
    essay = str(change) + '\n' + content
    file.seek(0)
file.writelines(essay)
file.close()
# 21.1.8  小文件复制
# 打开一个已有文件，读取完整内容，并写入到另外一个文件
file = open('L12test.py', mode='r+', encoding='utf-8')
file2 = open('21.1.8output.py', mode='r+', encoding='utf-8')
copies = file.read()
print(copies)
file2.writelines(copies)
# 21.1.9  大文件复制
# 打开一个已有文件，逐行读取内容，并顺序写入到另外一个文件
file = open('L12test.py', mode='r+', encoding='utf-8')
file2 = open('21.1.9output.py', mode='r+', encoding='utf-8')
copies = ''.join(file.readlines())
file2.writelines(copies)

