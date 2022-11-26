# - 允许用户输入 1 次成绩（0-100）、最多两位小数（可以是整数）
# - 如果输入的数字不符合要求，抛出自定义异常 ScoreError
# 在主程序中，完成 30 名学生成绩的录入，并捕获 2 类异常
# 1. 输入的不是数字
# 2. 输入的数字不符合要求
class ScoreError(Exception):
    pass


def record(n):
    n1 = str(n)
    for i in range(0, len(n1)):
        if n1[i] == '.':
            n1 = n1[i+1::]
            break
    if 0 <= n <= 100 and len(n1) <= 2:
        return n
    else:
        raise ScoreError

i = 0
while i < 29:
    for i in range(i, 30):
        try:
            print(i)
            n = float(input("scores:"))
            print(record(n))
        except ScoreError:
            print('ScoreError')
            break
        except Exception:
            print('ScoreError')
            break
