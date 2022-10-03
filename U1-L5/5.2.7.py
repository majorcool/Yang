# 5.2.7 系统里面有多个用户，用户的信息目前保存在元祖中(一一对应），完成简单的登录功能
# 提示用户输入用户名和密码
# 如果登录成功，打印欢迎消息
# 如果失败，说明具体的错误原因，让用户重新登陆，共有 3 次机会
users = ('root', 'user1', 'user2')
passwords = ('123', 'abc', '@*#')
try_num = 0
while try_num < 3:
    name = str(input("请输入用户名"))
    if name == users[0]:
        password = int(input("请输入密码"))
        if password == 123:
            print("密码正确")
            break
        else:
            try_num += 1
            print("密码错误")
            continue
    if name == users[1]:
        password = str(input("请输入密码"))
        if password == "abc":
            print("密码正确")
            break
        else:
            try_num += 1
            print("密码错误")
            continue
    if name == users[2]:
        password = str(input("请输入密码"))
        if password == "@*#":
            print("密码正确")
            break
        else:
            try_num += 1
            print("密码错误")
            continue
    else:
        print("用户名错误")
        try_num += 1
        continue
if try_num >= 3:
    print("三次机会用完了")