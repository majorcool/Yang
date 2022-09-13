# 1.3.4 使用 input() 输入你的姓名、性别、学号，按照下方格式打印所有信息（左右对齐即可）
n = input("姓名：")
f = input("性别：")
h = input("学号：")
print("---- info ----")
print("Name:%9s" % n)
print("Gender:%7s" % f)
print("ID:%11s" % h)
print("--------------")