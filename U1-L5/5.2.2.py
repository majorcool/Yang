# 5.2.2 编写一个函数，功能是计算学生的平均分
# 用户先输入正整数 n，告知学生数量
# 用户输入每个学生的成绩，如果成绩在 0-100 以外，提示用户输入错误
# 学生成绩录入完毕后，计算平均分，将平均分作为返回值
# 在函数外部调用函数，打印出学生的平均分
def nnn():
    sum=0
    n = int(input("请输入学生数量（正整数）:"))
    a = 0
    while a < n:
        x = float(input("成绩:"))
        if 0<=x<=100:
            a = a + 1
            sum = sum + x
        else:
            print("错误请重新输入")
    return sum / n
print(nnn())