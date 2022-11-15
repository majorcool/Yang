def gcd_pro_max_2(n:list):
    while 1:
        for a in range(0,len(n)-1):
            if n[a] % n[a+1] == 0:
                n.pop(a)
                n.append(n[a+1])
                n.pop(a+1)
                n.append(n[a+1])
            else:
                b = n[a] % n[a+1]
                n.pop(a)
                n.append(b)
                n.pop(a+1)
                n.append(n[a+1])
        count = 0
        for b in range(0,len(n)-1):
            if n[b] == n[b+1]:
                count =+ 1
        if count == len(n)-1:
            break
    print(n[0])
gcd_pro_max_2([15,6,9])