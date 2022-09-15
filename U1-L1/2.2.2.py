# 2.2.2 思考学校生活中有没有逻辑嵌套的场景，仿照 #2.2.1（变量赋值、打印等），实现代码逻辑
r = str(input("witch lunch do you want,A or B?"))
if r == "A" :
    r2 = input("how many do you want,1 or 2?")
    if r2 == 1 :
        print(28)
    else :
        print(35)
else :
    print(38)