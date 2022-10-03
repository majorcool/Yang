# 5.2.8 编写一个函数，功能是去除元祖中的重复项（默认都是数字类型的元素），升序排列后，返回新的元祖
# 比如 tuple_sample = (1, 1, 2, 3, 6, 5, 4, 1)，返回 (1, 2, 3, 4 ,5 ,6)
tuple1=(1,3,4,3,4,5,6,1,2,3,3,4,7)
tuple1=list(tuple1)
tuple1.sort()
a=-999
b=[]
for n in range(0,len(tuple1)):
    if a!=tuple1[n]:
        b.append(tuple1[n])
    a=tuple1[n]
b=tuple(b)
print(b)