# 5.1.6 定义一个函数，将列表每隔一个元素就增加一个 0，将新列表作为返回值
list=[1,2,3,4,5,6,7,8,9]
def nnn():
    z=len(list)
    for n in range(0,2*z):
        if n%2!=0:
            s=(n+1)/2
            s=int(s)
            list.insert(n,"0"*s)
        else:
            p=n/2+1
            p=int(p)
            list[n]=p
    return list
print(nnn())


