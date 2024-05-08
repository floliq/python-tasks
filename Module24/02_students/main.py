class Student:

    def __init__(self, fullname, group, marks):
        self.fullname = fullname
        self.group = group
        self.marks = marks

    def get_avarage(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def get_student_info(self):
        return 'ФИ: {}, Группа {}, ср балл {}'.format(
            self.fullname,
            self.group,
            self.get_avarage()
        )


students_list = [
    Student('Петров Иван', 31, [5, 5, 5, 5, 1]),
    Student('Иванов Петр', 32, [3, 5, 5, 3, 5]),
    Student('Сидоров Илья', 35, [5, 5, 5, 3, 5]),
    Student('Ильин Сидор', 22, [5, 5, 5, 4, 5]),
    Student('Александров Алексей', 14, [3, 3, 5, 5, 5]),
    Student('Алексеев Александр', 12, [5, 5, 5, 5, 5]),
    Student('Пупкин Василий', 15, [5, 5, 5, 5, 3]),
    Student('Васильев Пупок', 31, [5, 5, 5, 3, 5]),
    Student('Ефремов Иннокентий', 16, [5, 3, 5, 3, 5]),
    Student('Клубничка Виктория', 45, [5, 5, 5, 3, 5]),
]
sorted_students = sorted(students_list, key=lambda student:student.get_avarage())
for index, student in enumerate(sorted_students):
    print('{}: {}'.format(index + 1, student.get_student_info()))
