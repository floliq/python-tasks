name_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
print("Элементы списка с четным индексом:", end=" ")
for i in range(len(name_list)):
    if i % 2 == 0:
        print(name_list[i], end=" ")

# зачтено
