import random

items = [random.randint(1,10) for _ in range(10)]
print("Оригинальный список: {}".format(items))
new_list1 = [(items[i], items[i + 1]) for i in range(0, len(items), 2)]
print("Новый список: {}".format(new_list1))
new_list1 = [pair for pair in zip(items[::2], items[1::2])]
print("Новый список: {}".format(new_list1))
