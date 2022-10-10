list1=[-1,0,1,2,-1,-4]
result=[]
for a in range(0,len(list1)-2):
    for b in range(a+1,len(list1)-1):
        for c in range(b+1,len(list1)):
            if list1[a]+list1[b]+list1[c]==0:
                x,y,z=list1[a],list1[b],list1[c]
                tuple1=tuple(sorted((x,y,z)))
                result.append(tuple1)
result=set(result)
print(result)

