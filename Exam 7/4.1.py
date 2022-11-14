def gcd_pro_max_2(* n:int):
    list1=[]
    while 1:
        for a in range(0,len(n)-1):
            if n[a] % n[a+1] == 0:
                list1.append(n[a+1])
                list1.append(n[a+1])
            else:
                b = n[a] % n[a+1]
                list1.append(b)
                list1.append(n[a+1])
        for b in list1:

gcd_pro_max_2(122333)