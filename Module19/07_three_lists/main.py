def solution_one():
    print('Задача 1:')
    array = [num for num in array_1 if num in array_2 and num in array_3]
    print_results('- Решение без множеств: ', array)
    intersection = set_array_1 & set_array_2 & set_array_3
    print_results('- Решение с множествами: ', intersection)


def solution_two():
    print('Задача 2:')
    array = [num for num in array_1 if num not in array_2 and num not in array_3]
    print_results('- Решение без множеств: ', array)
    difference = set_array_1 - set_array_2 - set_array_3
    print_results('- Решение с множествами: ', difference)


def print_results(string, array):
    print(string, end='')
    for num in sorted(array):
        print(num, end=' ')
    print()


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
set_array_1, set_array_2, set_array_3 = set(array_1), set(array_2), set(array_3)
solution_one()
print('\n')
solution_two()
