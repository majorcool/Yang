# 21.1.1  文件指针位置
# 使用 open() 函数打开文件并读取文件中的内容时，总是会从文件的第一个字符（字节）开始读起。那么，有没有办法可以指定读取的起始位置呢？
# 借助搜索引擎查询解决方案，配合代码体现成果
file = open('L12test.py', encoding='utf-8', mode='r+')
file.seek(2)
print(file.readlines())
file.close()