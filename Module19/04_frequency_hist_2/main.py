def get_dist():
    for char in text:
        freq_dist_1[char] = freq_dist_1.get(char, 0) + 1
    for key in sorted(freq_dist_1.keys()):
        print('{0} : {1}'.format(key, freq_dist_1[key]))


def get_invert_dist():
    for key, value in freq_dist_1.items():
        freq_dist_2.setdefault(value, []).append(key)
    for key in freq_dist_2:
        print('{0} : {1}'.format(key, freq_dist_2[key]))


text = input('Введите текст: ')
freq_dist_1 = dict()
freq_dist_2 = dict()
print('Оригинальный словарь частот:')
get_dist()
print('\nИнвертированный словарь частот:')
get_invert_dist()
