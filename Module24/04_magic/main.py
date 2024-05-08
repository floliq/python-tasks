class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None


class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None



class Storm:

    def __str__(self):
        return 'Шторм'

    def __add__(self, other):
        return None


class Vapor:

    def __str__(self):
        return 'Пар'

    def __add__(self, other):
        return None


class Dirt:

    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        return None


class Lightning:

    def __str__(self):
        return 'Молния'

    def __add__(self, other):
        return None


class Dust:

    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        return None


class Lava:

    def __str__(self):
        return 'Лава'

    def __add__(self, other):
        return None


water = Water()
air = Air()
fire = Fire()
earth = Earth()
storm = Storm()
dirt = Dirt()
lightning = Lightning()
dust = Dust()
lava = Lava()
print(f'{water} + {air} = {water + air}')
print(f'{water} + {fire} = {water + fire}')
print(f'{water} + {earth} = {water + earth}')
print(f'{air} + {fire} = {air + fire}')
print(f'{air} + {earth} = {air + earth}')
print(f'{fire} + {earth} = {fire + earth}')
print(f'{storm} + {earth} = {storm + earth}')
