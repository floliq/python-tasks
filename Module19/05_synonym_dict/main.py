words = {}
count = int(input('Введите количество пар слов: '))
for i in range(count):
    pair_word1, pair_word2 = input('{} пара:'.format(i + 1)).lower().split(' — ')
    words[pair_word1], words[pair_word2] = pair_word2, pair_word1
while True:
    word = input('Введите слово: ').lower()
    if word in words:
        print('Синоним: {}'.format(words[word].capitalize()))
        break
    else:
        print('Такого слова в словаре нет.')
