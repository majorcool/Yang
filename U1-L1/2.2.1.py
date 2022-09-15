# 2.2.1 用两种不同的逻辑嵌套方式，完成火车站安检的例子
ticket = False
knife = True
#first opnion
if ticket == True :
    if knife == True :
        print("get out of my sight prisoner")
    else :
        print("welcome")
else :
    print("why you dont buy the ticket")

#second opnion
if ticket == True and knife == False :
    print("welcome")
elif ticket == False :
    print("why you dont buy the ticket")
elif knife== True :
    print("get out of my sight prisoner")