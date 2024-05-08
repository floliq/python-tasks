def summa(n):
    summ = 0
    while n != 0:
        summ += n % 10
        n //= 10
    return summ


def count_num(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count


n = int(input("Введите число: "))
summ = summa(n)
print(f"Сумма цифр: {summ}")
count = count_num(n)
print(f"Кол-во цифр в числе: {count}")
result = summ - count
print(f"Разность суммы и кол-ва цифр: {result}")

