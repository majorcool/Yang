#Exam 类包含 4 个实例属性：id，start_time，end_time，points
#Test 类继承自 Exam 类，不同的是，Test 类不包含起始和终止时间，points 属性永远为 10
class Exam:
    def __init__(self,id,points,end_time,start_time):
        self.id=id
        self.points=points
        self.start_time=start_time
        self.end_time=end_time


class Test(Exam):
    def change(self):
        del self.end_time
        del self.start_time
        self.points=10


a=Exam(1,2,3,4)
b=Test(5,6,7,8)
print(a.end_time)
print(a.points)
b.change()
print(b.points)
print(b.end_time)#报错证明已删除
