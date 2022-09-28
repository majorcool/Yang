# 5.2.4 定义一个元祖类型的购物车，用户可以不断的输入想添加的商品，输入 'q' 结束，打印出当前购物车中商品的数量，以及所有的商品
n=0
b=0
list1=[]
while n!="q":
    n=input()
    list1.append(n)
    b=b+1
b=b-1
list1.pop()
print(b)
print(list1)