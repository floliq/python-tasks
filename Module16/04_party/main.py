guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
act = ""
while act != "Пора спать":
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    act = input("Гость пришёл или ушел? ")
    if act == "пришел":
        name = input("Имя гостя: ")
        if len(guests) <= 5:
            guests.append(name)
            print(f"Привет, {name}!")
        else:
            print(f"Прости, {name}, но мест нет.")
    elif act == "ушел":
        name = input("Имя гостя: ")
        if name in guests:
            guests.remove(name)
            print(f"Пока, {name}")
        else:
            print("У нас нет такого человека на вечеринке!")
    print()
print("Вечеринка закончилась, все легли спать.")

