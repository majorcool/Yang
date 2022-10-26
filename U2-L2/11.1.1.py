class Student:
    def __init__(self):
        self.name=input("name:")
        self.ID=input("ID:")
        self.course=input("course(用逗号隔开):").split(",")
    def get_course(self):
        print(self.course)
    def __len__(self):
        print("已选{}节课".format(len(self.course)))
    def print(self):
        print("{} {}".format(self.name,self.ID))
    def __del__(self):
        print("已删除学生：{}   {}".format(self.name,self.ID))
student_1=Student()
student_1.print()
student_1.get_course()
len(student_1.course)
del student_1