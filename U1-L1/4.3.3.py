# 4.3.3 改写 #4.2.3：函数内不打印消息，将消息作为函数的返回值。调用 3 次函数，分别传入不同的参数，打印出不同的消息。并且，使用 2 种调用的方式
def make_shirt(a="I love python"):
    return a
b=make_shirt("ji")
c=make_shirt()
print("大号%s" % b)
print("中号%s" % c)
print("中号短袖",end="")
print(make_shirt("7777"))
