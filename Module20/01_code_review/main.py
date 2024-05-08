students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def get_hobbies_and_surname_len(students_dict):
    interests_set = set()
    surname_len = 0
    for student in students_dict.values():
        surname_len += len(student['surname'])
        interests_set.update(student['interests'])
    return interests_set, surname_len

        
pairs_id_age = [(num, age['age']) for num, age in students.items()]
interests, surname_length = get_hobbies_and_surname_len(students)
print('Список пар "ID студента - Возраст":', pairs_id_age)
print('Полный список интересов всех студентов:', set(interests))
print('Общая длина всех фамилий студентов:', surname_length)
