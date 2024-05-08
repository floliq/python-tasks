def count_unique_characters(text: str) -> int:
    """
    Функция расчета количества уникальных символов в строке
    """

    message = text.lower()
    return len(list(filter(lambda letter: message.count(letter) == 1, message)))


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
