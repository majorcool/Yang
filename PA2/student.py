#   2. 登录、退出系统


class Student:
    student_num = []

    def __init__(self, username, password):
        Student.student_num.append(self)
        print('{} student account has been created'.format(username))
        self.state = False
        self.username = username
        self.password = password
        self.course = []

    def login(self, username, password):  # 登录
        if username in Student.student_num:
            if password == Student.student_num[username]:
                print('Login succeeded')
                self.state = True
            else:
                print('password are not accord with username')
        else:
            print('The user is not registered')

    def out(self):  # 退出
        self.state = False
        print('sign out succeed')

    @staticmethod
    def check_score_requirement(administration_class):  # 查看学分要求
        print(administration_class.score_requirement)

    @staticmethod
    def check_course_message(course_num):  # 查看课程信息
        for i in course_num:
            print('{}:number{}{} teacher{} max_people{}'.format(i.username, i.number, i.number_list, i.teacher, i.max_people))

    def choose_course(self, new_course):  # 选课 ->interact
        self.course.append(new_course)

    def remove_course(self, old_course):  # 退课 ->interact
        self.course.remove(old_course)
