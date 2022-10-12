# 6.1.5 定义一个函数，参数为 1 个字符串，分别统计出其中英文字母、空格、数字和其它字符的个数，将所有数量保存在 1 个元祖返回
num=input("num")
b,c,d,e=0,0,0,0
len1=len(num)
for n in range(0,len1):
    a=num[n]
    if a.isspace():
        b+=1
    elif a.isalpha():
        c+=1
    elif a.isnumeric():
        d+=1
    else:
        e+=1
tuple1=("num:{},space:{},alpha:{},another:{}".format(c,b,d,e))
print(tuple1)