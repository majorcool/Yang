def num(n):
    n=int(n)
    num=bin(n)
    print(num)
    sum=""
    for n in range(0,32-len(num)):
        sum="0"+sum
    sum=sum+str(num)
    sum=sum[::-1]
    sum.replace("b","0")
    sum="0b"+sum
    sum=sum[:32]
    print(sum)
    sum=int(sum)
    print(sum)
num(3)