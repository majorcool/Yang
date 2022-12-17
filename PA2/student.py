#   2. 登录、退出系统
import os
import atexit


class Student:
    student_num = []
    for i in list(os.listdir('students')):
        with open(str(i), 'r') as f:
            content = f.read().split('\n')[0]
            student_num.append(content)

    def __init__(self, username, password):
        Student.student_num.append(str(self))
        self.state = False
        self.score_goal_achievement = False
        self.credits_selected = 0
        self.username = username
        self.password = password
        self.course = []
        open('students/{}'.format(self.username), 'w').close()
        with open('students/{}'.format(self.username), 'w') as stu:
            stu.write(str(self))
            stu.write('\n')
            stu.write(str(self.password))
            stu.write('\n')
            stu.write(str(self.course))
            stu.write('\n')
            stu.write(str(self.score_goal_achievement))
            stu.write('\n')
            stu.write(str(self.credits_selected))
        print('{} student account has been created'.format(username))
        atexit.register(self._del)

    def _del(self):
        with open('students/{}'.format(self.username), 'w') as stu:
            stu.write(str(self))
            stu.write('\n')
            stu.write(str(self.password))
            stu.write('\n')
            stu.write(str(self.course))
            stu.write('\n')
            stu.write(str(self.score_goal_achievement))
            stu.write('\n')
            stu.write(str(self.credits_selected))

    @staticmethod
    def check_score_requirement(administration_class):  # 查看学分要求
        print(administration_class.score_requirement)

    @staticmethod
    def check_course_message(course_num):  # 查看课程信息
        for i in course_num:
            print('{}:number{}{} teacher{} max_people{}'.format(i.username, i.number, i.number_list, i.teacher, i.max_people))

    def choose_course(self, new_course):  # 选课 ->interact finish
        self.course.append(new_course)
        print('{} Successful course selection'.format(self.username))

    def remove_course(self, old_course):  # 退课 ->interact finish
        self.course.remove(old_course)

