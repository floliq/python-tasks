def tpl_sort(tpl):
    for num in tpl:
        if type(num % (num // 1)) is not int:
            return tpl
    return tuple(sorted(tpl))
        

tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))
