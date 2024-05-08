def reverse_int(num):
    num //= 1
    number = 0
    while num > 0:
        number = number * 10 + num % 10
        num //= 10
    return number


def get_float(num):
    num = str(num)
    new_float = ""
    flag = False
    for char in num:
        if char == ".":
            flag = True
        elif char != "." and flag:
            new_float += char
        else:
            continue
    return new_float


def reverse_float(num):
    num = int(num)
    number = 0
    while num > 0:
        number = number * 10 + num % 10
        num //= 10
    return number


def new_number(int_num, float_num):
    count = 0
    for char in str(float_num):
        count += 1
    float_num /= 10 ** count
    num = int_num + float_num
    return num


num1 = float(input("Введите первое число:"))
num2 = float(input("Введите второе число:"))
int_num1 = reverse_int(num1)
float_num1 = reverse_float(get_float(num1))
num1 = new_number(int_num1, float_num1)
int_num2 = reverse_int(num2)
float_num2 = reverse_float(get_float(num2))
num2 = new_number(int_num2, float_num2)
result = num1 + num2
print(f"Сумма: {result}")

