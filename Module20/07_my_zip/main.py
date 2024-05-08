def shortest_range(string, tpl):
    return min(len(string), len(tpl))


symbs = 'abcd'
tup = (10, 20, 30, 40)
pairs = ((symbs[i], tup[i]) for i in range(shortest_range(symbs, tup)))
print(pairs)
for elem in pairs:
    print(elem)