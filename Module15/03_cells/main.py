n = int(input("Кол-во клеток: "))
cells_list = []
for cell in range(1, n + 1):
    efficiency = int(input(f"Эффективность {cell} клетки: "))
    cells_list.append(efficiency)
print("Неподходящие значения:", end=" ")
for i in range(len(cells_list)):
    if cells_list[i] < i:
        print(cells_list[i], end=" ")

# зачтено
