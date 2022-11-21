#  def do_sth_good_to_live_longer(**staffs: Staff) -> None:
'''加个self'''
# employees.append()
'''employees list can't find 应先定义一个employees列表，再在括号中加上employee()'''

# Boss 类定义了 2 个内置方法，4 个实例可以调用的方法
# Employee 类的构造函数有 4 个必选参数，实例化时最多能传入 4 个参数
# Boss 类的 do_sth_good_to_live_longer() 方法中，可以传入 字典 类型的参数
# Employee 类的构造函数调用了 0 次，Boss 类的 work() 方法调用了 6 次
# boss 和 employee 都调用了 work() 方法，且有不同的效果，体现了work的多态性

# [1,2,3,4,5]
# 13579

# 根据文档中的说明，解释上方代码中的现象
'''type会根据数据原本的类型进行判断，所以False在bool中是False
   而isinsitance会在两者不同类别时返回True'''
# 文档中提到，推荐使用 isinstance() 进行变量类型的判断，为什么？
'''type在判断时会跟原来的类进行对比，但是当原来的类是新的类的父类时，子类继承原有父类的所有属性，但type判断新子类和父类相比时返回False
，所以说他只会判断对象是否属于python内置的类，从而于python鸭子类相违背，导致判断错误；而isinstance会根据两者的属性进行判断。'''
