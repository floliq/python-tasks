violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

n = int(input("Сколько песен выбрать? "))
time = 0

for i in range(n):
    name_song = input(f"Название {i + 1} песни: ")
    for song in violator_songs:  # TODO сделайте же распаковку :)
        if song[0] == name_song:
            time += song[1]

print(f"Общее время звучания песен: {round(time, 2)}")

