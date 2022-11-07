def num(n):
    n = bin(n)
    print(n)
    n = str(n)
    n = n[2::]
    while len(n) < 32:
        n = "0" + n
    n = n[::-1]
    n = "0b" + n
    n = int(n, 2)
    return n


num_0 = 43
print(num(num_0))