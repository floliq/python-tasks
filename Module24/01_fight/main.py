import random


class Warrior:

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.damage = 20

    def attack(self, enemy):
        enemy.hp -= self.damage
        enemy.hp = max(0, enemy.hp)
        print('{} нанес игру {} {} урона. У него осталось {} hp'.format(
            self.name, enemy.name, self.damage, enemy.hp
        ))
        if enemy.hp == 0:
            print('Победил {}'.format(self.name))


player1 = Warrior('Игрок 1')
player2 = Warrior('Игрок 2')
while player1.hp > 0 and player2.hp > 0:
    turn = random.randint(1, 2)
    if turn == 1:
        player1.attack(player2)
    else:
        player2.attack(player1)
