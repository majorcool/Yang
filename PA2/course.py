class Course:
    course_num = []

    def __init__(self, name, teacher, credit, max_people):
        self.name = name
        self.teacher = teacher
        self.credit = credit
        self.number = 0
        self.number_list = []
        self.max_people = max_people
        print('{} course has been created'.format(self.name))


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


a = ElectiveCourse(1, 2, 3, 4)
print(a.number, ElectiveCourse.elective_count)
