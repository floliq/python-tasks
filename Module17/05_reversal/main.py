text = input("Введите строку: ")
lft_part = text[:text.index("h")]
ctr_part = text[text.index("h"):text.rindex("h") + 1]
rgt_part = text[text.rindex("h") + 1:]
result = lft_part + ctr_part[::-1] + rgt_part
print(result)

# TODO Принято! Покажу другой вариант:
string = input('Введите строку: ')
h_index_1 = 0
for sym in string:
    if sym == 'h':
        break
    h_index_1 += 1

h_index_2 = len(string) - 1
for sym in string[::-1]:
    if sym == 'h':
        break
    h_index_2 -= 1

between = string[h_index_1 + 1:h_index_2]
reverse_between = between[::-1]

print('Развернутая последовательность между первым и последним h:', reverse_between)
