def caeser(text, shift):
    char_list = [(alphabet[(alphabet.index(char) + shift) % 33]
                  if char != " " else " ")
                 for char in text]
    result = "".join(char_list)
    return result


alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
word = input("Введите сообщение: ")
step = int(input("Введите сдвиг: "))
output = caeser(word, step)
print(output)
