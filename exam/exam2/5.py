num=0
for n in range(2,1000):
    for a in range(1,n):
        if n%a == 0:
            num=num+a
    if num==n:
        print(num)
    num=0