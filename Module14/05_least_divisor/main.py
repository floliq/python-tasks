def lower_divisor(n):
    i = 1
    while i <= n:
        i += 1
        if n % i == 0:
            return i


n = int(input("Введите число: "))
result = lower_divisor(n)
print(f"Наименьший делитель, отличный от единицы: {result}")
