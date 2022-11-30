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


