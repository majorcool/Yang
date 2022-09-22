a=0
b=0
c=0
d=0
e=0
f=0
for n in range(100,1000):
    a=int(n/10)
    g=n%a
    z=int(n/100)
    s=(n-g)/10-z*10

    if n==g**3+s**3+z**3:
        print(n)

