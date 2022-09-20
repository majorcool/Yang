# 3.1.10 分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
n=int(input("请输入数字:"))
print(n ,end=" = ")
for a in range(2,n+1) :
    if n%a==0 :
        print(a,end=" * ")
        n=n/a
print("1")

