# 21.1.10  调整缩进
# 某个没有素质的 Python 学习者使用了不规范的空格进行缩进，有的地方使用 2 个空格缩进，有的地方使用 3 个，但是保证了同一个代码块中的缩进是对齐的，因此可以正常运行
# 他将 .py 发给你（文件作为示例），希望你编写一个程序，能够自动将所有不规范的缩进按照 PEP8 的建议修改缩进格式，并保存到新文件中
file = open('21.1.10output.py', mode='r+', encoding='utf-8')
file.writelines('a = 1\nfor i in range(10):\n    a += 1\n    print(a)\n    for i in range(10):\n        a -= 1\n        print(a)\n        if a == 5:\n            print(a)\n            break\n        else:\n            if a == 7:\n                print(a)\n                break\nprint(a)''')
file.close()

