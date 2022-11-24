# 定义一个函数，函数的参数为一个字符串，获取用户的输入
# 主程序中，用户一次性输入 5 个数，以逗号分隔
# 函数需要将用户输入的数字提取出来，存入列表并返回这个列表
# 如果输入数据不为整数，要捕获产生的异常，打印 '请输入整数'
# 捕获输入参数不足 5 个或超过 5 个的异常，打印 '请输入 5 个整数'
class ErrorLength(Exception):
    pass


def define(n:str):
    n = n.split(',')
    if len(n) != 5:
        raise ErrorLength
    for i in range(0, len(n)):
        n[i] = int(n[i])
    print(n)


try:
    define('123,3,5,4,6')
except ErrorLength:
    print('请输入 5 个整数')
except ValueError:
    print('请输入整数')
