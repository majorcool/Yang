# 21.1.8  小文件复制
# 打开一个已有文件，读取完整内容，并写入到另外一个文件
file = open('L12test.py', mode='r+', encoding='utf-8')
file2 = open('21.1.8output.py', mode='r+', encoding='utf-8')
copies = file.read()
print(copies)
file2.writelines(copies)

