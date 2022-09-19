# 3.1.10 分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
n = int(input("请输入数字:"))
a=2
print(n,end=" =")
while n != 1:
    while n % a == 0 :
        n= n/a
        print(" %d"% a,end=" *")
    a=a+1
print(" 1")