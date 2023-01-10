# 3.2.10 分解质因数：用户输入一个正整数，用程序进行分解质因数，如输出 30 = 2 * 3 * 5
n=int(input("请输入数字:"))
print(n ,end=" = ")
while n>1:
    for a in range(2, n+1):
        if n % a == 0 :
            n = n / a
            n = int(n)
            if n==1:
                print(a)
                break
            else:
                print(a, end=" * ")
                break


