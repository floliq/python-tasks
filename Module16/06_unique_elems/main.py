def input_values(list_name, counter):
    for i in range(counter):
        item = int(input(f"{i + 1}-й элемент списка: "))
        list_name.append(item)


first_list, second_list = [], []
print("Первый список")
input_values(first_list, 3)
print("Первый список")
input_values(second_list, 7)
print("Первый список: ", first_list)
print("Второй список: ", second_list)
first_list.extend(second_list)
first_list = list(set(first_list))
print("Новый первый список с уникальными элементами: ", first_list)
