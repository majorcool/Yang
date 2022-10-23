def reciprocal(n):
    n = str(n)
    if len(n) == 1:
        return n
    else:
        return n[0] + reciprocal(n[1:])
print(reciprocal(123456789)[::-1])
