def iosiph_algoritm(distance):
    skip = distance - 1
    index = skip % len(persons_list)
    while len(persons_list) > 1:
        print("Текущий круг людей: ", persons_list)
        print("Начало счета с номера ", index)
        print(f"Выбывает человек с номером {persons_list[index]}")
        persons_list.remove(persons_list[index])
        index = (index + skip) % len(persons_list)
        print()
    print(f"Остался человек с номером {persons_list[0]}")


n = int(input("Количество человек: "))
persons_list = list(range(1, n + 1))
k = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {k}й человек")
iosiph_algoritm(k)
