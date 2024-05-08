import math


def get_sage_sqrt(num):
    try:
        result = math.sqrt(num)
        return result
    except ValueError as e:
        return 'Отрицательно число {}'.format(e)
    except Exception  as e:
        return 'Некорректные данные {}'.format(e)


numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
