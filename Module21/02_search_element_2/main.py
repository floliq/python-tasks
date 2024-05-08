site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_value(tree, key, depth=None):
    if depth is None:
        depth = float('inf')
    elif depth <= 0:
        return None
    if key in tree:
        return tree[key]
    for sub_tree in tree.values():
        if isinstance(sub_tree, dict):
            result = find_value(sub_tree, key, depth - 1)
            if result:
                break
    else:
        result = None
    return result


key = input('Введите искомый ключ: ')
req = input('Хотите ввести максимальную глубину? Y/N: ').lower()
depth = None
if req == "y":
    depth = int(input('Введите максимальную глубину: '))
value = find_value(site, key, depth)
print('Значение ключа: {}'.format(value))
