import os
import atexit


class Course:
    course_num = list(os.listdir('courses'))

    def __init__(self, attribute, name, teacher, credit, max_people):
        Course.course_num.append(str(self))
        self.attribute = attribute  # 0选修，1必修
        self.name = name
        self.teacher = teacher
        self.credit = credit
        self.number = 0
        self.number_list = []
        self.max_people = max_people
        open('courses/{}'.format(self.name), 'w').close()
        with open('courses/{}'.format(self.name), 'w') as cor:
            cor.write(self.attribute)
            cor.write('\n')
            cor.write(str(self))
            cor.write('\n')
            cor.write(self.teacher)
            cor.write('\n')
            cor.write(str(self.credit))
            cor.write('\n')
            cor.write(str(self.number))
            cor.write('\n')
            cor.write(str(self.number_list))
            cor.write('\n')
            cor.write(str(self.max_people))
        atexit.register(self._del)

    def _del(self):
        with open('courses/{}'.format(self.name), 'w') as cor:
            cor.write(self.attribute)
            cor.write('\n')
            cor.write(str(self))
            cor.write('\n')
            cor.write(self.teacher)
            cor.write('\n')
            cor.write(str(self.credit))
            cor.write('\n')
            cor.write(str(self.number))
            cor.write('\n')
            cor.write(str(self.number_list))
            cor.write('\n')
            cor.write(str(self.max_people))


class RequiredCourse(Course):
    require_count = 0

    def __init__(self, name, teacher, credit, max_people):
        super().__init__(name, teacher, credit, max_people)
        RequiredCourse.require_count += 1


class ElectiveCourse(Course):
    elective_count = 0

    def __init__(self, name, teacher, credit, max_people):
        super().__init__(name, teacher, credit, max_people)
        ElectiveCourse.elective_count += 1



