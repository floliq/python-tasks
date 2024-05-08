cols, rows = 3, 4
new_list = [list(range(x, x + rows * (cols - 1) + 1, rows))
            for x in range(1, rows + 1)]
print(new_list)
