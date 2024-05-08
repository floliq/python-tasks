def print_file(filename):
    print('Содержимое файла {}'.format(filename))
    file = open(filename)
    for line in file:
        print(line, end='')
    print()
    file.close()


def get_analysis(text):
    letters_dict = dict()
    letters =  [letter for letter in text if letter.isalpha()]
    letters_count = len(letters)
    for letter in letters:
        letters_dict[letter] = letters_dict.get(letter, 0) + 1 / letters_count
    letters_dict = dict(sorted(letters_dict.items(), key=lambda x: (-x[1], x[0])))
    file_name = 'analysis.txt'
    file = open(file_name, 'w')
    for key in letters_dict.keys():
        file.write('{} : {:.3f}\n'.format(key, letters_dict[key]))
    file.close()
    print_file(file_name)
    

def get_text(file_name):
    print_file(file_name)
    file = open(file_name)
    text = file.read().lower()
    file.close()
    get_analysis(text)


file_name = 'text.txt'
get_text(file_name)
