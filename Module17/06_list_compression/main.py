import random

n = int(input("Введите размер списка: "))
zeros_count = 0
old_list = [random.randint(0, 2) for i in range(n)]
print("Список:", old_list)
new_list = [value for value in old_list if value > 0]
for _ in range(len(old_list) - len(new_list)):
    new_list.append(0)
# TODO можно было сделать всё на одном for итерируя по числу длины списка удалять нули с помощью remove и сразу
#  добавлять их обратно с помощью append
print("Список с 0 в конце:", new_list)
if 0 in new_list:
    new_list = new_list[:new_list.index(0)]
print("Конечный результат", new_list)
