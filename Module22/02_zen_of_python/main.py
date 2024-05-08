def get_reversed_file(filename):
    file = open(filename)
    lines = [line.replace('\n', '') for line in file]
    file.close()
    for line in reversed(lines):
        print(line)


get_reversed_file('zen.txt')
