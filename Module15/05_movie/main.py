films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
print(f"Список всех фильмов: {films}")
favourite_films = []
film = ""
while film != "end":
    film = input("Введите название фильма: ")
    if film in films and film not in favourite_films:
        print(f"Фильм {film} добавлен в список любимых фильмов")
        favourite_films.append(film)
    elif film in favourite_films:
        print("Такой фильм уже есть в списке любимых фильмов, введите другой фильм")
    else:
        print("Данного фильма нет в списке фильмов, попробуйте ввести фильм еще раз")
print("Список любимых фильмов: ", favourite_films)

# зачтено
