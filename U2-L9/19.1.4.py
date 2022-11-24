# 定义一个函数，参数为半径 r，计算圆的面积
# 自定义一个异常类 RadiusError，如果半径为负值，抛出 RadiusError
class RadiusError(Exception):
    pass


def area(r):
    if r < 0:
        raise RadiusError
    return (r * r) * 3.14


try:
    print(area(-1))
except RadiusError:
    print('RadiusError')
except Exception as a:
    print(a)
