import time
count=["empty"," "," "," "," "," "," "," "," "," "]
again=False
def form(a,b):
    o1 = count[1]
    t2 = count[2]
    t3 = count[3]
    f4 = count[4]
    f5 = count[5]
    s6 = count[6]
    s7 = count[7]
    e8 = count[8]
    n9 = count[9]
    if a==0:
        if b==1 and count[b]==" ":
            o1="X"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==2 and count[b]==" ":
            t2="X"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==3 and count[b]==" ":
            t3="X"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==4 and count[b]==" ":
            f4="X"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==5 and count[b]==" ":
            f5="X"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==6 and count[b]==" ":
            s6="X"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==7 and count[b]==" ":
            s7="X"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==8 and count[b]==" ":
            e8="X"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==9 and count[b]==" ":
            n9="X"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
    if a==1:
        if b==1 and count[b]==" ":
            o1="O"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==2 and count[b]==" ":
            t2="O"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==3 and count[b]==" ":
            t3="O"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==4 and count[b]==" ":
            f4="O"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==5 and count[b]==" ":
            f5="O"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==6 and count[b]==" ":
            s6="O"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==7 and count[b]==" ":
            s7="O"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==8 and count[b]==" ":
            e8="O"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==9 and count[b]==" ":
            n9="O"
            print("丨", o1, "丨", t2, "丨", t3, "丨", sep=" ")
            print("丨", f4, "丨", f5, "丨", s6, "丨", sep=" ")
            print("丨", s7, "丨", e8, "丨", n9, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
black_player=input("请输入玩家1姓名（先手X）：")
white_player=input("请输入玩家2姓名（后手O）：")
begin=True
print("填入数字即可将对应的格子填上自己的图案")
print("丨 (1) 丨 (2) 丨 (3) 丨")
print("丨 (4) 丨 (5) 丨 (6) 丨")
print("丨 (7) 丨 (8) 丨 (9) 丨")
print("")
time.sleep(1)
n=1
while n<=8:
        if n%2!=0:
            while 1:
                num = int(input("请X方输入数字："))
                if type(num)==int and 1<=num<=9:
                    break
                else:
                    print("输入的字符不符合要求，请重新输入")
            accept=form(0,num)
            if accept!=1:
                n=n+1
            if count[1] == count[2] == count[3] == "X" or count[4] == count[5] == count[6] == "X" or count[7] == count[8] == count[9] == "X" or count[1] == count[4] == count[7] == "X" or count[2] == count[5] == count[8] == "X" or count[3] == count[6] == count[9] == "X" or count[1] == count[5] == count[9] == "X" or count[3] == count[5] == count[7] == "X":
                time.sleep(1)
                print("%s赢了"% black_player)
                begin = False
                break
        if n%2!=1:
            while 1:
                num = int(input("请O方输入数字："))
                if type(num)==int and 1<=num<=9:
                    break
                else:
                    print("输入的字符不符合要求，请重新输入")
            accept = form(1, num)
            if accept != 1:
                n = n + 1
            if count[1] == count[2] == count[3] == "O" or count[4] == count[5] == count[6] == "O" or count[7] == count[8] == count[9] == "O" or count[1] == count[4] == count[7] == "O" or count[2] == count[5] == count[8] == "O" or count[3] == count[6] == count[9] == "O" or count[1] == count[5] == count[9] == "O" or count[3] == count[5] == count[7] == "O":
                time.sleep(1)
                print("%s赢了" % white_player)
                begin = False
                break