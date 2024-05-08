def check_word(text):
    list_sym = list(text)
    new_list = []
    for char in list_sym:
        counter = 1
        for i in range(list_sym.index(char) + 1, len(list_sym)):
            if char == list_sym[i]:
                counter += 1
        if counter == 1:
            new_list.append(char)
    return len(new_list)


word = input("Введите слово: ")
count = check_word(word)
print("Кол-во уникальных букв: ", count)

# зачтено
