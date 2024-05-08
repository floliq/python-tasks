def print_file(filename):
    print('Содержимое файла {}'.format(filename))
    file = open(filename)
    for line in file:
        print(line, end='')
    print()
    file.close()


def get_sorted_qualified_file(lst):
    lst.sort(key=lambda x: x[-1], reverse=True) 
    file = open('second_tour.txt', 'w')
    file.write('{}\n'.format(len(lst)))
    for index, el in enumerate(lst):
        name = '{}.'.format(el[1][0])
        file.write('{0}) {1} {2} {3}\n'.format(
            index + 1,
            name,
            el[0],
            el[2]
        ))
    file.close()
    print_file('second_tour.txt')


def get_qualified(filename):
    print_file(filename)
    qualified = list()
    file = open(filename)
    k = 0
    for index, line in enumerate(file):
        info = line.split()
        if index == 0:
            k = int(info[0])
        elif int(info[-1]) > k:
            qualified.append(info)
    file.close()
    get_sorted_qualified_file(qualified)


get_qualified('first_tour.txt')
