# 21.1.9  大文件复制
# 打开一个已有文件，逐行读取内容，并顺序写入到另外一个文件
file = open('L12test.py', mode='r+', encoding='utf-8')
file2 = open('21.1.9output.py', mode='r+', encoding='utf-8')
copies = ''.join(file.readlines())
file2.writelines(copies)
