# 5.1.1 为以下列表尝试以上 14 种方法 / 函数 / 关键字，每一步操作后，打印当前的列表
num_list = [1, 2, 3, 4, 5]
num_list.insert(0, 0)
print('step 0 :', num_list)

num_list.append(6)
print(num_list)

list2=[7,8,9]
num_list.extend(list2)
print(num_list)

del num_list[0]
print(num_list)

del num_list
#print(num_list)
num_list=[0,1,2,3,4,5,6,7,8,9]
print(num_list)

num_list.remove(0)
print(num_list)

num_list.pop(0)
print(num_list)

num_list.clear
print(num_list)

num_list=[1,2,3,4,5,6,7,8,9]
num_list[0]=7
print(num_list)

num_list.sort()
print(num_list)

num_list.sort(reverse=True)
print(num_list)

num_list.reverse()
print(num_list)

n=len(num_list)
print(n)

z=num_list.count(7)
print(z)
