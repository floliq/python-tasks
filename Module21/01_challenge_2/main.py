def get_nums(num):
    if num > 1:
        get_nums(num - 1)
    print(num)


num = int(input('Введите num:'))
get_nums(num)
