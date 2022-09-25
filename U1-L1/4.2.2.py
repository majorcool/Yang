# 4.2.2 编写一个名为 make_shirt() 的函数，用户输入尺码以及要印到短袖上的文字。这个函数应打印一个句子，告知用户短袖的尺码和文字，便于用户确认
def make_shirt():
    s=int(input("尺码:"))
    t=input("请输入文字:")
    print("尺码%d,文字%s"%(s,t))
make_shirt()