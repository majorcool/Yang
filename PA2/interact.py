from administration import Administration
from course import Course
from student import Student


class Interact:
    def __init__(self):
        pass

    @staticmethod
    def create_student_account_interact(username, password):
        Administration.create_student_account(username)
        Student(username, password)

    @staticmethod
    def create_course_interact(name, teacher, goal_score, max_people):
        Administration.create_course(name)
        Course(name, teacher, goal_score, max_people)

    @staticmethod
    def choose_course_interact(student_instance, new_course):
        student_instance.choose_course(new_course)
        new_course.mumber += 1
        new_course.number_list.append(student_instance)

    @staticmethod
    def remove_course_interact(student_instance, old_course):
        student_instance.remove_course(old_course)
        old_course.mumber -= 1
        old_course.mumber_list.remove(student_instance)
    @staticmethod
    def judge(student_instance):
        if student_instance.credits_selected > Administration.score_requirement:
            student_instance.score_goal_achievement = True
        else:
            pass

# a = Interact()  Test
# b = Interact()
# a.create_student_account_interact('name', 3)
# b.create_student_account_interact('name', 3)
# print(Student.student_num)












