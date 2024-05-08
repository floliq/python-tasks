skates_list = []
legg_list = []
n = int(input("Кол-во коньков: "))
for i in range(n):
    size = int(input(f"Размер {i + 1} пары:"))
    skates_list.append(size)
k = int(input("Кол-во людей: "))
for i in range(k):
    size = int(input(f"Размер ноги {i + 1} человека:"))
    legg_list.append(size)
print(skates_list)
print(legg_list)
counter = 0
for i in legg_list:
    for j in range(len(skates_list)):
        if skates_list[j] >= i:
            skates_list.remove(skates_list[j])
            counter += 1
            break
print("Наибольшее кол-во людей, которые могут взять ролики:", counter)
