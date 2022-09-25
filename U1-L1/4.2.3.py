# 4.2.3 修改 #4.2.2 中的函数 make_shirt()，使其在默认情况下制作一件印有 "I love Python" 的短袖。调用这个函数 3 次，分别制作 1 件大号短袖，
# 印有 "I love Python"；1 件中号短袖，印有 "I love Python"；1 件小号短袖，印有任意其它文字
def make_shirt(a="I love python"):
    print(a)

print("大号",end="")
make_shirt()
print("中号",end="")
make_shirt()
print("中号短袖77777777777777")
