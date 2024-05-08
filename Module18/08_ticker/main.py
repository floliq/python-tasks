def running_str(text1, text2):
    step = 0
    is_valid = True
    while text1 != text2:
        step += 1
        text1 = text1[-1:] + text1[:-1] 
        if step > len(text1) - 1:
            is_valid = False
            break
    if is_valid:
        print('Первая строка получается из второй со сдвигом {}.'.format(step))
    else:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


text1 = input('Первая строка: ')
text2 = input('Вторая строка: ')
running_str(text1, text2)
