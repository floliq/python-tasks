text = input('Введите строку: ').lower()
words = text.split()
words = [word.capitalize() for word in words]
new_text = " ".join(words)
print('Результат: {}'.format(new_text)) 
