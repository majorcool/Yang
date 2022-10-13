list_input=[]
list_input1=input("list")
len1=len(list_input1)
for n in range(0,len1):
    a=list_input1[n]
    list_input.append(a)
while 1:
    x=int(input("x"))
    if 0<x<=len1:
        break
    else:
        print("请输入正确x")
dir="right"
while 1:
    dir=input("dir(left or right or skip):")
    if dir == "left" or dir =="right":
        break
    elif dir=="skip":
        dir="right"
        break
    else:
        print("请输入正确dir")
count=x
if dir=="right":
    for z in range(0,count):
        num = list_input[-count]
        list_input.pop()
        list_input.insert(0,num)
if dir=="left":
    for o in range(0,count):
        num = list_input[count-1]
        list_input.pop(0)
        list_input.append(num)
print(list_input)



