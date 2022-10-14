login_info={"kunkun":["pw1"]}
list1=[]
listpw=[]
def login():
    for n in range(0,3):
        while 1:
            while 1:
                pw1 = input("pw1")
                if pw1=="q":
                    print("False")
                    return
                if pw1.isalnum() and len(pw1) >= 8 and pw1.isnumeric()==False and pw1.isalpha()==False:
                    print("输入正确")
                    break
                else:
                    if pw1.isnumeric() == False:
                        print("devoid number")
                    elif len(pw1) < 8:
                        print("too short")
                    else:
                        print("devoid alpha")
            if pw1 in login_info.values():
                print("请设置新密码")
            else:
                print("success")
                listpw.append(pw1)
                login_info[user1]=listpw
                break
    listpw[::-1]
    list1.insert(3-n,pw1)
while 1:
    user1=input('user:')
    if user1=="q":
        print("False")
        break
    if user1 in login_info.keys():
        list1.append(user1)
        login()
        break
    else:
        print("try again")
print(list1)
print(login_info)
