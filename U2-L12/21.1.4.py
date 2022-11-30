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

