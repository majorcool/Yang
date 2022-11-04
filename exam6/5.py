#列举你认为课程应该具有的属性和方法，并进行代码实现
class Course:
    def __init__(self,difficult,score,name,people):
        self.difficult=difficult
        self.score=score
        self.name=name
        self.people=people
    def __del__(self):
        print("{}课程已删除".format(self.name))
    def people_num(self):
        print("{}有{}人".format(self.name,self.people))
math=Course(3,100,"math",20)
math.people_num()
del math