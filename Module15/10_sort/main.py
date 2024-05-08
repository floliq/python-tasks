def sort_nums(list_num):
    i_min = 0
    for i_min in range(len(list_num)):
        for curr in range(i_min, len(list_num)):
            if list_num[curr] < list_num[i_min]:
                list_num[curr], list_num[i_min] = list_num[i_min], list_num[curr]


list_nums = [1, 4, -3, 0, 10]
print(f"Изначальный список: {list_nums}")
sort_nums(list_nums)
print(f"Отсортированный список:: {list_nums}")

# зачтено
