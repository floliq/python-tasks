def sum(*args):
    res = 0
    for x in args:
        if isinstance(x, list):
            res += sum(*x)
        else:
            res += x
    return res


#print(sum([[1, 2, [3]], [1], 3]))
#print(sum(1, 2, 3, 4, 5))
