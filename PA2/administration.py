#   1. 登录、退出系统


class Administration:
    administration_num = []
    score_requirement = ''

    def __init__(self, username, password):
        Administration.administration_num.append(self)
        print('{} administration account has been created'.format(username))
        self.state = False
        self.username = username
        self.password = password

    def login(self, username, password):  # 登录
        if username in Administration.administration_num:
            if password == Administration.administration_num[username]:
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
    def check_student_message(student_num):  # 查看学生账号信息
        for i in student_num:
            print('{}:course{}'.format(i.username, i.course))

    @staticmethod
    def create_student_account(student_class, username, password):  # 创建学生账号 ->interact
        student_class.student_num.append(student_class(username, password))
        print('{}account has been create successfully'.format(username))

    @staticmethod
    def create_course(course_class, name, teacher, goal_score, max_people):  # 创建课程 ->interact
        course_class.course_num.append(course_class(name, teacher, goal_score, max_people))

    @staticmethod
    def change_course_name(course_instance, new_message):  # 修改课程name
        course_instance.name = new_message

    @staticmethod
    def change_course_teacher(course_instance, new_message):  # 修改课程teacher
        course_instance.teacher = new_message

    @staticmethod
    def change_course_credit(course_instance, new_message):  # 修改课程credit
        course_instance.credit = new_message

    @staticmethod
    def change_max_people(course_instance, new_message):  # 修改课程max_people
        course_instance.max_people = new_message

    @staticmethod
    def check_course_message(course_num):  # 查看课程信息
        for i in course_num:
            print('{}:number{}{} teacher{} max_people{}'.format(i.username, i.number, i.number_list, i.teacher, i.max_people))

    @classmethod
    def set_target(cls, target):  # 设置学生的学分要求
        cls.score_requirement = target
        print('new target{} has been set')

    @ staticmethod
    def check_student_class(course_nums: list):  # 查看学生选课情况
        for i in course_nums:
            print('{}:{}{}'.format(i.name, i.number, i.number_list))
