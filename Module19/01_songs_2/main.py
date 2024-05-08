violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


music_count = int(input('Сколько песен выбрать? '))
total = 0
for i in range(music_count):
    music_name = input('Название {0} песни: '.format(i + 1))
    if music_name in violator_songs:
        total += violator_songs[music_name]
    else:
        print('Неверное название песни!')
print('Общее время звучания песен: {0:.2f}'.format(total))
