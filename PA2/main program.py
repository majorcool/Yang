from administration import Administration
from course import Course
from interact import Interact
from student import Student
import os


def run():
    username = ''
    mode = int(input('请选择登录端：（1）students    （2）administrations'))
    while 1:
        if mode in range(1, 2):
            break
        mode = int(input('输入不符合要求,请重新输入:'))

    if mode == 1:
        while 1:
            username = input('username:')
            if username in os.listdir('students'):
                break
            print('用户名错误')
        while 1:
            password = input('password:')
            with open('students/{}'.format(username), 'r') as f:
                content = f.read().split('\n')
                if content[1] == password:
                    break

        while 1:
            mode = int(input('(1)查看学分要求   (2)查看课程信息   (3)选课   (4)退课   (5)退出'))
            while 1:
                if mode in range(1, 6):
                    break
                mode = int(input('输入不符合要求,请重新输入:'))

            if mode == 1:
                Student.check_score_requirement(Administration)

            if mode == 2:
                Student.check_course_message(Course.course_num)

            if mode == 3:
                with open('students/{}'.format(username), 'r') as f:
                    student_instance = f.read().split('\n')[0]
                with open('students/{}'.format(username), 'r') as f:
                    studemt_cor = list(f.read().split('\n')[2])
                    while 1:
                        new_course = input('请输入一门想选择的课程：')
                        if new_course in Course.course_num:
                            with open('courses/{}'.format(new_course), 'r') as f1:
                                course_num = int(f1.read().split('\n')[4])
                            with open('courses/{}'.format(new_course), 'r') as f1:
                                course_max = int(f1.read().split('\n')[6])
                                if course_max == course_num:
                                    print('课程已满')
                                elif new_course in studemt_cor:
                                    print('您已选过该课程')
                                else:
                                    print('选课成功')
                                    break
                        else:
                            print('该课程未创建')
                    with open('courses/{}'.format(new_course), 'r') as f1:
                        course_instance = f1.read().split('\n')[1]
                        print(student_instance)
                    Interact.choose_course_interact(student_instance, course_instance)
                    with open('courses/{}'.format(new_course), 'r') as f1:
                        if int(f1.readline().split('\n')[4]) >= Administration.score_requirement:
                            student_instance.score_goal_achievement = True

            if mode == 4:
                with open('students/{}'.format(username), 'r') as f:
                    student_instance = f.read().split('\n')[0]
                with open('students/{}'.format(username), 'r') as f:
                    studemt_cor = list(f.read().split('\n')[2])
                    while 1:
                        new_course = input('请输入一门退选择的课程：')
                        if new_course in Course.course_num:
                            if new_course in studemt_cor:
                                print('退课成功')
                                break
                            else:
                                print('您未选过该课程')
                        else:
                            print('该课程未创建')
                        with open('courses/{}'.format(new_course), 'r') as f:
                            course_instance = f.read().split('\n')[1]
                        with open('students/{}'.format(username), 'r') as f:
                            student_instance = f.read().split('\n')[0]
                        Interact.choose_course_interact(student_instance, course_instance)
                        if int(f1.read().split('\n')[4]) >= Administration.score_requirement:
                            student_instance.score_goal_achievement = True

            if mode == 5:
                print('已成功退出登录')
                break

    if mode == 2:
        while 1:
            username = input('username:')
            if username in os.listdir('administrations'):
                break
            print('用户名错误')
        while 1:
            password = input('password:')
            with open('administrations/{}'.format(username), 'r') as f:
                content = f.read().split('\n')
                if content[1] == password:
                    break

        while 1:
            mode = int(input('(1)创建学生账号   (2)查看学生账号信息   (3)设置学生的学分要求   (4)创建课程   (5)修改课程信息   (6)查看课程   (7)查看学生的选课情况'))
            while 1:
                if mode in range(1, 2):
                    break
                mode = int(input('输入不符合要求,请重新输入:'))

            if mode == 1:
                username = input('username:')
                password = input('password:')
                Interact.create_student_account_interact(username, password)

            if mode == 2:
                Administration.check_student_message(Student.student_num)

            if mode == 3:
                while 1:
                    target = input('请输入目标分数:')
                    if target.isnumeric() and 0 < int(target):
                        break
                    print('请输入正整数')
                Administration.set_target(target)

            if mode == 4:
                attribute = input('attribute')
                name = input('name:')
                teacher = input('teacher:')
                goal_score = input('goal_score:')
                max_people = input('max_people:')
                Interact.create_course_interact(attribute, name, teacher, goal_score, max_people)

            if mode == 5:
                while 1:
                    course = input('course:')
                    if course in os.listdir('courses'):
                        break
                    print('课程未创立')
                with open('courses') as f:
                    output = input('max:')
                    Administration.change_max_people(f.read().split('\n')[1], output)
                with open('courses') as f:
                    output = input('max:')
                Administration.change_course_credit(f.read().split('\n')[1], output)
                with open('courses') as f:
                    output = input('max:')
                Administration.change_course_name(f.read().split('\n')[1], output)
                with open('courses') as f:
                    output = input('max:')
                Administration.change_course_teacher(f.read().split('\n')[1], output)

            if mode == 6:
                Administration.check_course_message(Course.course_num)

            if mode == 7:
                Administration.check_student_class(Course.course_num)



A = Student('1', '2')
B = Course('1', '2', '3', '4', '5')
run()

