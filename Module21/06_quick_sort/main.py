def qsort(user_list):
    if len(user_list) <= 1:
        return user_list
    else:
        el, more_list, less_list, equal_list = user_list[-1], [], [], []
        for num in user_list:
            if num < el:
                less_list.append(num)
            elif num > el:
                more_list.append(num)
            else:
                equal_list.append(num)
    return qsort(less_list) + equal_list + qsort(more_list)


custom_list = [5, 8, 9, 4, 2, 9, 1, 8]
result = qsort(custom_list)
print(result)
