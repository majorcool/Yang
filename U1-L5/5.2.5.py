# 5.2.5 处理矩阵
# 使用 for 循环，将下方的矩阵保存在一个二维列表中
# 定义 2 个元祖，一个保存行，一个保存列，元祖的每个元素是一个列表（一行或一列的所有数），打印这 2 个元祖
# 定义 2 个新的元祖，分别保存行、列的和，打印这 2 个元祖
'''
  1  2  3  4  5  6
  7  8  9 10 11 12
 13 14 15 16 17 18
 19 20 21 22 23 24
 25 26 27 28 29 30
 31 32 33 34 35 36
'''
d=[]
h=[]
for a in range(0,6):
    c=a
    c=[]
    for b in range(a*6+1,6*a+7):
        c.append(b)
    d.append(c)
print(d)
d=tuple(d)
print(d)
e=1
for f in range(0,6):
    g=f
    g=[]
    while e<37:
        g.append(e)
        e=e+6
    e=f+2
    h.append(g)
h=tuple(h)
print(h)
d=list(d)
h=list(h)
p=0
for i in range(0,len(h)):
    for o in d[i]:
        p=p+o
    del h[i]
    h.insert(i,p)
print(h)
q=0#不知为何不对
for r in range(0,len(d)):
    for s in d[r]:
        q=q+s
    del d[r]
    d.insert(r,q)
print(r)
