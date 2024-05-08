length = int(input("Введите длину списка: "))  # TODO Не использовали в программе
result = [(1 if num % 2 == 0 else num % 5) for num in range(10)]
print("Результат: ", result)

