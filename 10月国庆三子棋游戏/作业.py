import time
import os
count = ["empty"," "," "," "," "," "," "," "," "," "]
piece = {1: {"a":"","b":""},2: {"a":"","b":""},3: {"a":"","b":""},4: {"a":"","b":""},5: {"a":"","b":""},6: {"a":"","b":""},7: {"a":"","b":""},8: {"a":"","b":""},9: {"a":"","b":""}}
again = False
def form (a,b):
    one = count[1]
    two = count[2]
    three = count[3]
    four = count[4]
    five = count[5]
    six = count[6]
    seven = count[7]
    eight = count[8]
    nine = count[9]
    if a==0:
        if b==1 and count[b]==" ":
            one="X"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==2 and count[b]==" ":
            two="X"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==3 and count[b]==" ":
            three="X"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==4 and count[b]==" ":
            four="X"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==5 and count[b]==" ":
            five="X"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==6 and count[b]==" ":
            six="X"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==7 and count[b]==" ":
            seven="X"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==8 and count[b]==" ":
            eight="X"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==9 and count[b]==" ":
            nine="X"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="X"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
    if a==1:
        if b==1 and count[b]==" ":
            one="O"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==2 and count[b]==" ":
            two="O"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==3 and count[b]==" ":
            three="O"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==4 and count[b]==" ":
            four="O"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==5 and count[b]==" ":
            five="O"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==6 and count[b]==" ":
            six="O"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==7 and count[b]==" ":
            seven="O"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==8 and count[b]==" ":
            eight="O"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
        if b==9 and count[b]==" ":
            nine="O"
            print("丨", one, "丨", two, "丨", three, "丨", sep=" ")
            print("丨", four, "丨", five, "丨", six, "丨", sep=" ")
            print("丨", seven, "丨", eight, "丨", nine, "丨", sep=" ")
            print("")
            count[b]="O"
            return
        elif count[b]!=" ":
            print("该位置已被下过，请重下")
            again=True
            return 1
while 1:
    black_player = input("请输入玩家1姓名（先手X）：")
    white_player = input("请输入玩家2姓名（后手O）：")
    begin = True
    print("填入数字即可将对应的格子填上自己的图案")
    print("丨 (1) 丨 (2) 丨 (3) 丨")
    print("丨 (4) 丨 (5) 丨 (6) 丨")
    print("丨 (7) 丨 (8) 丨 (9) 丨")
    print("")
    time.sleep(1)
    time1 = 1
    while 1:
        method = int(input("请输入数字’1‘or’2‘，1为简单模式；2为复杂模式："))
        if method == 1 or method == 2:
            break
    if method == 2:
        while begin != False:
            if time1 % 2 != 0:
                os.system("cls")
                while 1:
                    num = int(input("请X方输入数字："))
                    if type(num) == int and 1 <= num <= 9:
                        break
                    else:
                        print("输入的字符不符合要求，请重新输入")
                accept = form(0, num)
                if accept != 1:
                    piece[time1] = {"a": "X", "b": num}
                    time1 = time1 + 1
                if count[1] == count[2] == count[3] == "X" or count[4] == count[5] == count[6] == "X" or count[7] == \
                        count[8] == count[9] == "X" or count[1] == count[4] == count[7] == "X" or count[2] == count[
                    5] == count[8] == "X" or count[3] == count[6] == count[9] == "X" or count[1] == count[5] == count[
                    9] == "X" or count[3] == count[5] == count[7] == "X":
                    time1.sleep(1)
                    print("%s赢了" % black_player)
                    begin = False
                    break
                if time1 > 6:
                    value1 = piece[time1 - 6]["a"]
                    value2 = piece[time1 - 6]["b"]
                    print("{}在第{}格即将消失".format(value1, value2))
                    print("")
                    count[piece[time1 - 6]["b"]] = " "
            if time1 % 2 != 1:
                os.system("cls")
                while 1:
                    num = int(input("请O方输入数字："))
                    if type(num) == int and 1 <= num <= 9:
                        break
                    else:
                        print("输入的字符不符合要求，请重新输入")

                accept = form(1, num)
                if accept != 1:
                    piece[time1] = {"a": "O", "b": num}
                    time1 = time1 + 1
                if count[1] == count[2] == count[3] == "O" or count[4] == count[5] == count[6] == "O" or count[7] == \
                        count[8] == count[9] == "O" or count[1] == count[4] == count[7] == "O" or count[2] == count[
                    5] == count[8] == "O" or count[3] == count[6] == count[9] == "O" or count[1] == count[5] == count[
                    9] == "O" or count[3] == count[5] == count[7] == "O":
                    time1.sleep(1)
                    print("%s赢了" % white_player)
                    begin = False
                    break
                if time1 > 6:
                    value1 = piece[time1 - 6]["a"]
                    value2 = piece[time1 - 6]["b"]
                    print("{}在第{}格即将消失".format(value1, value2))
                    print("")
                    count[piece[time1 - 6]["b"]] = " "
    if method == 1:
        end = 1
        while begin != False and time1 <= 9:
            if time1 % 2 != 0:
                while 1:
                    num = int(input("请X方输入数字："))
                    if type(num) == int and 1 <= num <= 9:
                        break
                    else:
                        print("输入的字符不符合要求，请重新输入")
                accept = form(0, num)
                if accept != 1:
                    piece[time1] = {"a": "X", "b": num}
                    time1 = time1 + 1
                if count[1] == count[2] == count[3] == "X" or count[4] == count[5] == count[6] == "X" or count[7] == \
                        count[8] == count[9] == "X" or count[1] == count[4] == count[7] == "X" or count[2] == count[
                    5] == count[8] == "X" or count[3] == count[6] == count[9] == "X" or count[1] == count[5] == count[
                    9] == "X" or count[3] == count[5] == count[7] == "X":
                    time.sleep(1)
                    print("%s赢了" % black_player)
                    begin = False
                    end = 0
                    break
            if time1 % 2 != 1:
                if time1 == 10:
                    break
                while 1:
                    num = int(input("请O方输入数字："))
                    if type(num) == int and 1 <= num <= 9:
                        break
                    else:
                        print("输入的字符不符合要求，请重新输入")
                accept = form(1, num)
                if accept != 1:
                    piece[time1] = {"a": "O", "b": num}
                    time1 = time1 + 1
                if count[1] == count[2] == count[3] == "O" or count[4] == count[5] == count[6] == "O" or count[7] == \
                        count[8] == count[9] == "O" or count[1] == count[4] == count[7] == "O" or count[2] == count[
                    5] == count[8] == "O" or count[3] == count[6] == count[9] == "O" or count[1] == count[5] == count[
                    9] == "O" or count[3] == count[5] == count[7] == "O":
                    time.sleep(1)
                    print("%s赢了" % white_player)
                    begin = False
                    end = 0
                    break
        if end == 1:
            print("平局")