from administration import Administration
from course import Course
from course import RequiredCourse
from course import ElectiveCourse
from student import Student
import os


def run():
    mode = int(input('请选择登录端：（1）students    （2）administrations'))
    while 1:
        if mode in range(1, 2):
            break
        mode = int(input('输入不符合要求,请重新输入:'))
    if mode == 1:
        while 1:
            username = input('username:')
            if username in os.listdir('students'):
                def a():
                    global user
                    user = username
                break
            print('用户名错误')
        while 1:
            password = input('password: ')
            with open('students/{}'.format(username), 'r') as f:
                while 1:
                    content = f.readline().split('\n')
                    if content[1] == password:
                        break
                    password = input('密码与账号不符，请重新输入')

    mode = int(input('(1)查看学分要求   (2)查看课程信息   (3)选课   (4)退课   (5)退出'))
    while 1:
        if mode in range(1, 5):
            break
        mode = int(input('输入不符合要求,请重新输入:'))
    while 1:
        if mode == 1:
            Student.check_score_requirement(Administration)

        if mode == 2:
            Student.check_course_message(Course.course_num)

        if mode == 3: #  变量无法引用
            with open('students/{}'.format(user), 'r') as f:

        if mode == 4: #  问题同上
            pass

        if mode == 5:
            print('已成功退出登录')
            break






