# 5.1.3 依次删除下方列表中所有的 3，并在删除后打印每个 3 的索引，最后打印最终的列表
# list_num = [1, 3, 4, 3, 7, 3, 9, 8, 6, 3]
list=[1,3,4,3,7,3,9,8,6,3]
n=list.count(3)
g=[]
for a in range(0,n):
    b=list.index(3)
    list.remove(3)
    list.insert(b,0)
    print(b)
for r in range(0,n):
    list.remove(0)
print(list)