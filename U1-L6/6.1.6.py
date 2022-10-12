# 6.1.6 定义一个函数，参数为 1 个字符串，将 a-z, A-Z 改为 z-a, Z-A，返回新的字符串
# 例如，参数为 'abcABC'，返回 'zyxZYX'
num=input("num")
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
len1=len(num)
for n in range(0,len1):
    a=num[n]
    if a.isupper():
        n=1
    if a.islower():
        n=2
    a=a.lower()
    b=alpha.index(a)
    c=alpha[-b-1]
    if n==1:
        c=c.upper()
        print(c,end="")
    if n==2:
        print(c,end="")