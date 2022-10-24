user_info={"password":"a1234567A"}
password_list=["a1234567A"]
def info():
    a = 0
    b = 0
    c = 0
    password = input("password:")
    while 1:
        if password == "1":
            break
        else:
            password = input("again password:")
    for G in range(0,2):
        newpassword=input("newpassword:")
        while 1:
            if newpassword.isalnum() and len(newpassword)>=8:
                for n in range(0,len(newpassword)):
                    if newpassword[n].isupper():
                        a=1
                    elif newpassword[n].isnumeric():
                        b=1
                    else:
                        c=1
                if a+b+c>=2:
                    if G==1:
                        if password==password_list[0]:
                            password_list.append(newpassword)
                            break
                        else:
                            print("密码不同")
                else:
                    if a==0:
                        print("devoid upper")
                    if b==0:
                        print("devoid number")
                    if c==0:
                        print("devoid alpha")
            a=b=c=0
            newpassword = input("again newpassword:")
info()
