# TODO здесь писать код
def is_prime(number):
    if number > 1:
        for i_num in range(2, (number // 2) + 1):
            if number % i_num == 0:
                return False
        return True 
    else:
        return False


def crypto(obj):
    return [value for index, value in enumerate(obj) if is_prime(index)]


#user = [100, 200, 300, 'буква', 0, 2, 'а']
#user = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5}
#user = 'О Дивный Новый мир!'
user = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = crypto(user)
print(result)
