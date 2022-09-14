n1 = n2 = n3 = n4 = n5 = n6 = 0
number = int(input("请输入数字："))
number1 = number / 10
number2 = int(number1)
if number1 - number2 == 0 :
    n1 = 0 * 2
else:
    n1 = 1 * 2 ** 0

number3 = number2 / 10
number4 = int(number3)
if number3 - number4 == 0 :
        n2 = 0 * 2 ** 1
else:
        n2 = 1 * 2 ** 1

number5 = number4 / 10
number6 = int(number5)
if number5 - number6 == 0:
        n3 = 0 * 2 ** 2
else:
        n3 = 1 * 2 ** 2

number7 = number6 / 10
number8 = int(number7)
if number7 - number8 == 0:
        n4 = 0 * 2 ** 3
else:
        n4 = 1 * 2 ** 3

number9 = number8 / 10
number10 = int(number9)
if number9 - number10 == 0:
        n5 = 0 * 2 ** 4
else:
        n5 = 1 * 2 ** 4

number11 = number10 / 10
number12 = int(number11)
if number11 - number12 == 0:
        n6 = 0 * 2 ** 5
else:
        n6 = 1 * 2 ** 5

nz = n1 + n2 + n3 + n4 + n5 + n6
print("10进制得：%d" % nz)