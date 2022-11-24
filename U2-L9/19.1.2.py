list_1 = [1, 2, 3, 4]
try:
    print(list_1[2])
finally:
    print('index out of bound!')  # 无论如何都会执行
list_2 = [1, 2, 3, 4]
try:
    print(list_2[2])
except:  # 出现异常后捕获异常时执行的代码
    print('index out of bound!')