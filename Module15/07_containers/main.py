def add_containers(n):
    containers_list = []
    prev_container = 210
    while n > 0:
        container = int(input("Введите вес контейнера: "))
        if 200 >= container > 0 and container <= prev_container:
            containers_list.append(container)
            n -= 1
            prev_container = container
        elif prev_container <= container <= 200:
            print("Контейнер весит больше предыдущего")
        else:
            print("Контейнер весит больше 200 кг или меньше нуля кг")
    return containers_list


n = int(input("Кол-во контейнеров: "))
list = add_containers(n)
print(list)
value = int(input("Введите вес нового контейнера:"))
for i in range(len(list)):
    if list[i] < value:
        print("Номер, куда встанет новый контейнер: ", i + 1)
        break
else:
    print("Номер, куда встанет новый контейнер:", len(list) + 1)

# зачтено
