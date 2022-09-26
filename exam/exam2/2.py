while 1:
    n1 = float(input("数字1:"))
    n2 = float(input("数字2:"))
    a = input("请输入算法(+-*/):")
    if a=="+":
        num=n1+n2
        print(num)
    if a=="-":
        num=n1-n2
        print(num)
    if a=="*":
        num=n1*n2
        print(num)
    if a=="/" and n2!=0:
        num=n1/n2
        print(num)
    elif n2==0:
        print("除数不能为0")
