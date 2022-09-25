# 4.3.2 改写 #4.2.2：函数内不打印消息，将消息作为函数的返回值。调用函数时，在 print 语句中直接调用函数，打印提示信息
def make_shirt():
    s=int(input("尺码:"))
    t=input("请输入文字:")
    print("尺码%d,文字%s"%(s,t))
print(make_shirt())