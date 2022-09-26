"""转换 = input((int)"转换：")
print("你干嘛%d" % 转换)
num1 = input((float))
num2 = input(float)
#num1 = float(num1)
#num2 = float(num2)
num = num1 + num2
print(num)

q = 3.3
q = float(q)
q = int(q)
print(q)
print(num1,num2,sep="ji",end="h\n")
print(num1,num2,end="d\n")
print("%+-7.1f" %50)
print("%010.3f" % 3.1415926)"""
"""def aaa(n1,n2):
    return n1+n2

a=aaa(1,2)
print(a)"""
# 3.1.6 一次考试后，循环录入某班级 30 名学生的成绩，并计算平均分
# 如果分数超过 100 或小于 0，提示“分数有误，请重新输入”
# 30 名学生的成绩输入完成后，提示“录入完毕！平均分为 xx 分”，并结束程序
n=0
s=0
while n<30:
    n=float(input("成绩:"))
    if n>=0 and n<=100:
        for a in range(0,30):
            s=s+n
b=s/30
print(b)











