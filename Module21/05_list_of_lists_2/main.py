nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def get_new_list(lst):
    output = []
    for item in lst:
        if isinstance(item, list):
            output.extend(get_new_list(item))
        else:
            output.append(item)
    return output


print(get_new_list(nice_list))
print(get_new_list(nice_list))
