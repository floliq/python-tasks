n = int(input("Кол-во палок: "))
k = int(input("Кол-во бросков: "))
s = list("I" * n)
for i in range(1, k + 1):
    L_i = int(input(f"Бросок {i}. Сбиты палки с номера "))
    R_i = int(input("по номер "))
    s[L_i - 1:R_i] = ["." for _ in range(R_i - L_i + 1)]
print()
print("Результат:", "".join(s))
