#   1. 登录、退出系统
import os
import atexit


class Administration:
    administration_num = os.listdir('administrations')
    if len(administration_num) == 0:
        score_requirement = 0
    else:
        with open('administrations/{}'.format(administration_num[0]), 'r') as adm:
            if len(administration_num[0]) == 3:
                score_requirement = administration_num[0].split('\n')[len(administration_num)-1]
            else:
                score_requirement = 0

    def __init__(self, username, password):
        self.state = False
        self.username = username
        self.password = password
        open('administrations/{}'.format(self.username), 'w').close()
        with open('administrations/{}'.format(self.username), 'w') as adm:
            adm.write(str(self))
            adm.write('\n')
            adm.write(str(password))
            adm.write('\n')
            adm.write(str(Administration.score_requirement))
        Administration.administration_num.append(str(self))
        print('{} administration account has been created'.format(username))
        atexit.register(self._del)

    def _del(self):
        with open('administrations/{}'.format(self.username), 'w') as adm:
            adm.write(str(self))
            adm.write('\n')
            adm.write(str(self.password))
            adm.write('\n')
            adm.write(str(Administration.score_requirement))

    @staticmethod
    def check_student_message(student_num):  # 查看学生账号信息
        for i in student_num:
            print('{}:course{}'.format(i.username, i.course))

    @staticmethod
    def create_student_account(username):  # 创建学生账号 ->interact finish
        print('{} account has been create successfully'.format(username))

    @staticmethod
    def create_course(name):  # 创建课程 ->interact finish
        print('{} course has been created'.format(name))

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
        print('new target {} has been set'.format(target))

    @ staticmethod
    def check_student_class(course_nums: list):  # 查看学生选课情况
        for i in course_nums:
            print('{}:{}{}'.format(i.name, i.number, i.number_list))
