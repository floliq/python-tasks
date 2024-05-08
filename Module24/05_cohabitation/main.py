import random


class Human:

    def __init__(self, name, house):
        self.name = name
        self.hungry = 50
        self.house = house

    def eat(self):
        if self.house.food > 0:
            print('{} покушал'.format(self.name))
            self.hungry += 1
            self.house.food -= 1
        else:
            print('Невозможно поесть, в холодильнике нет еды')

    def go_to_shop(self):
        if self.house.money > 0:
            print('{} сходил в магазин'.format(self.name))
            self.house.food += 1
            self.house.money -= 1
        else:
            print('Невозможно купить поесть, нет денег')

    def work(self):
        print('{} поработал'.format(self.name))
        self.hungry -= 1
        self.house.money += 1

    def play(self):
        print('{} поиграл'.format(self.name))
        self.hungry -= 1

    def live_day(self, action):
        if self.hungry < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_to_shop()
        elif self.house.money < 50:
            self.work()
        elif action == 1:
            self.work()
        elif action == 2:
            self.eat()
        elif action in (3, 4, 5, 6):
            self.play()

    def is_die(self):
        if self.hungry == 0:
            print('{} умер'.format(self.name)) 
            return True
        return False


class House:

    def __init__(self):
        self.food = 50
        self.money = 0


home = House()
human = Human('Вася', home)
human2 = Human('Катя', home)
for i in range(1, 366):
    if human.is_die():
        break
    print('Day {}'.format(i))
    turn_human1, turn_human2 = random.randint(1, 6), random.randint(1, 6)
    human.live_day(turn_human1)
    human2.live_day(turn_human2)
    print('Голод {}: {}'.format(
        human.name,
        human.hungry,
    ))
    print('Голод {}: {}'.format(
        human2.name,
        human2.hungry,
    ))
    print('Еды в холодильнике: {}, денег в тумбочке {}\n'.format(
        home.food,
        home.money
    ))
