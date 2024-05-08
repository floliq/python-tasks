text = input("Введите текст: ")

letters = ["a", "о", "э", "е", "и", "ы", "у", "ё", "ю", "я"]

vowels_letters = [char for char in text if char in letters]
print("Список гласных букв: ", vowels_letters)
print("Длина списка: ", len(vowels_letters))
