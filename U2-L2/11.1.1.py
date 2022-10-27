class Student:
    def __init__(self, name, ID, course):
        self.name = name
        self.ID = ID
        self.course = course.split(",")

    def __del__(self):
        print("已删除学生：{}   {}".format(self.name, self.ID))

    def __len__(self):#不知为何不对
        return len(self.course)

    def __str__(self):
        return self.name

    def print(self):
        print("{} {}".format(self.name, self.ID))

    def get_course(self):
        print(self.course)


student_1 = Student("kun", "1234567", "PE,Math,English")
student_1.print()
student_1.get_course()
print(student_1.course)
print(len(student_1))
print(student_1)
del student_1
