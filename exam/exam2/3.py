m=int(input("正整数m:"))
n=int(input("正整数n:"))
a=1
num=0
numz=0
for n in range(n,0,-1):
    num=n*a*m
    numz=numz+num
    a=a*10
print(numz)
