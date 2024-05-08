count = int(input('Введите количество заказов: '))
data = dict()
for i in range(count):
    order = input('{} заказ: '.format(i + 1)).split()
    if order[0] not in data:
        data[order[0]] = {order[1]:int(order[2])}
    else:
        if order[1] in data[order[0]]:
            data[order[0]][order[1]] += int(order[2])
        else:
            data[order[0]][order[1]] = int(order[2])
for person in sorted(data):
    print('{}:'.format(person))
    for item in sorted(data[person]):
        print('\t{name}:{value}'.format(
            name=item,
            value=data[person][item]
        ))
