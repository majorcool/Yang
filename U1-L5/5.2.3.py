# 5.2.3 将 5.2.2 的函数复制过来，将返回值修改为一个元祖，这个元祖保存了所有学生的成绩
# 在函数外部调用函数，获取所有学生的成绩，打印出所有学生的成绩
# 在函数外部计算所有学生的平均分，打印一条消息显示平均分
# 你发现一个学生的成绩有错误，修改这个成绩，并重新计算平均分，打印
def nnn():
    sum=0
    n = int(input("请输入学生数量（正整数）:"))
    a = 0
    list=[]
    while a < n:
        x = float(input("成绩:"))
        if x >= 0 and x <= 100:
            a = a + 1
            list.append(x)
        else:
            print("错误请重新输入")
    return tuple(list)
tuple1=nnn()
print(tuple1)
s=0
for d in tuple1:
    s=s+d
s=s/len(tuple1)
print(s)
tuple2=(99,101,99)
tuple2=list(tuple2)
sm=0
for i in tuple2:
    if i>100 or i < 0:
        p=tuple2.index(i)
        tuple2[p]=float(input("请重新输入错误成绩:"))
for l in tuple2:
    sm=sm+l
print(sm/len(tuple2))