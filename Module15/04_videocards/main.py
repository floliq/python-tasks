n = int(input("Кол-во видеокарт: "))
cards_list = []
new_cards_list = []
for i in range(1, n + 1):
    card = int(input(f"{i}  Видеокарта: "))
    cards_list.append(card)
maximum = max(cards_list)
print("Старый список видеокарт:", cards_list)
for card in cards_list:
    if card != maximum:
        new_cards_list.append(card)
print("Новый список видеокарт:", new_cards_list)

# зачтено
