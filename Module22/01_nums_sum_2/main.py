def print_file(filename):
    print('Содержимое файла {}'.format(filename))
    file = open(filename)
    for line in file:
        print(line, end='')
    print()
    file.close()


def get_sum_file(filename, saved_file):
    file = open(filename)
    result = sum([int(num) for line in file for num in line.split()])
    file.close()
    file = open(saved_file, 'w')
    file.write('{}'.format(result))
    file.close()
    

print_file('numbers.txt')
get_sum_file('numbers.txt', 'answer.txt')
print_file('answer.txt')
