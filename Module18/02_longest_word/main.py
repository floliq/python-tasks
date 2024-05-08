def get_longest_word(user_words):
    longest_word = user_words[0]
    longest_len = len(longest_word)
    for word in user_words[1:]:
        word_len = len(word)
        if word_len > longest_len:
            longest_word = word
            longest_len = word_len
    return longest_word, longest_len


text = input('Введите строку: ')
words = text.split()
word, length = get_longest_word(words)
print("Самое длинное слово {word}, его длина {length}".format(
    word=word,
    length=length
))
