first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))
first_class.extend(second_class)
first_class.sort()
print(first_class)
