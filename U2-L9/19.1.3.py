# 定义一个函数，参数为两个数字 a，b，计算 a / b 的值
# 如果 b 等于零，抛出异常
def division(a, b):
    return a / b


try:
    print(division(1, 0))

# except ZeroDivisionError:
#     print("Divisor can't equal to 0")
except Exception as result:
    print(result)
