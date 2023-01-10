cont=0
num1=input("num1")
num2=input("num2")
list_num1=[]
list_num2=[]
sumnum1=""
sumnum2=""
if num2.isnumeric()==False or num1.isnumeric()==False:
    if num1.isnumeric() == False:
        for n in range(0, len(num1)):
            if num1[len(num1) - n - 1] != ".":
                list_num1.append(num1[len(num1) - n - 1])
                list_num2.append(0)
            else:
                break
    if num2.isnumeric() == False:
        for n in range(0, len(num2)):
            if num2[len(num2) - n - 1] != ".":
                list_num2.append(num2[len(num2) - n - 1])
                list_num1.append(0)
            else:
                break
    num1 = float(num1)
    num2 = float(num2)
    numsum = num1 - (num1 % 1) + num2 - (num2 % 1)
    sumnum1 = ""
    list_num1.reverse()
    list_num2.reverse()
    for n in list_num1:
        n = str(n)
        sumnum1 = sumnum1 + n
    sumnum2 = ""
    for n in list_num2:
        n = str(n)
        sumnum2 = sumnum2 + n
    print(sumnum2)
    if len(sumnum1)>len(sumnum2):
        diff=len(sumnum1)-len(sumnum2)
        sumnum2=sumnum2+diff*"0"
        print(sumnum2)
    elif len(sumnum1)==len(sumnum2):
        m=0
    else:
        diff=len(sumnum2)-len(sumnum1)
        sumnum1=sumnum1+diff*"0"
        print(sumnum1)
    sumfloat = int(sumnum2) + int(sumnum1)
    for n in range(0,len(list_num1)):
        list_num1[n]=int(list_num1[n])
    for n in range(0,len(list_num2)):
        list_num2[n]=int(list_num2[n])
    list_num1.sort(reverse=True)
    list_num2.sort(reverse=True)
    print(list_num2)
    print(list_num1)
    if int(list_num1[0]) + int(list_num2[0]) >= 10:
        numsum += 1
        sumfloat = str(sumfloat)[1::1]
    print("{}.{}".format(int(numsum), int(sumfloat)))
else:
    numsum=int(num1)+int(num2)
    print(numsum)

