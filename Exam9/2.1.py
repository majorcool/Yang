# 在 try……finally 结构中，无论 try 语句是否出现异常，finally 语句都会执行
# 在函数中，finally 的执行顺序在 return 之前还是之后？
# 设计一段代码，探究以上问题，在设计并运行代码后，用多行注释简单说明 finally 的执行机制
class except1(Exception):
    pass

def define1(n):
    if n == 5:
        raise except1
    return 'return'

try:
    print(define1(3))

except except1:
    pass
finally:
    print('finally')#若打出finally则表示先执行finally；否则先执行define
