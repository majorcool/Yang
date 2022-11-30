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
