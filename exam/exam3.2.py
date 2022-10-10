list=[1,2,-3,-3,0,9]
numz=0
result=[]
for a in range(0,len(list)-2):
    for b in range(1,len(list)-1):
        for c in range(2,len(list)):
            num=list[a]*list[b]*list[c]
            if num > numz:
                numz=num
                result=[list[a],list[b],list[c]]
print(numz)
print(result)