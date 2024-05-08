list = [1, 2, 3, 4, 5]
k = int(input("Введите количество шагов: "))
step = 1
while step <= k:
    print(f"Сдвиг {step}")
    n = list[-step:] + list[:-step]
    print(n)
    step += 1

# зачтено
