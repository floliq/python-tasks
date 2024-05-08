class Parent:
    calm = {True: 'спокоен', False: 'неспокоен'}
    hungry = {True: 'сытый', False: 'голодный'}

    def __init__(self, name, age, childs = []):
        self.name = name
        self.age = age
        self.childs = []
        for child in childs:
            if self.age - child.age < 16:
                print('\nНевозможно добавить ребенка {}, разница меньше 16 лет'.format(
                    child.name
                ))
            else:
                self.childs.append(child)
                print('{} добавлен к родителю {}'.format(
                    child.name,
                    self.name
                ))

    def say_about_youself(self):
        print('\n{} {}'.format(self.name, self.age))
        if self.childs:
            print('Дети:')
            for child in self.childs:
                print('{} {} лет, спокойствие: {}, сытость: {}'.format(
                    child.name,  
                    child.age, 
                    self.calm[child.is_calm], 
                    self.hungry[child.is_hungry]
                ))
        else:
            print('У {} нет детей'.format(self.name))
    
    def calm_down(self, child):
        if child not in self.childs:
            print('{} нет у родителя {}'.format(child.name, self.name))
        elif child.is_calm:
            print('{} уже спокойный'.format(child.name))
        else:
            child.is_calm = True
            print('{} успокоили'.format(child.name))

    def feed_child(self, child):
        if child not in self.childs:
            print('{} нет у родителя {}'.format(child.name, self.name))
        elif child.is_hungry:
            print('{} уже сыт'.format(child.name))
        else:
            child.is_hungry = True
            print('{} покормили'.format(child.name))


class Child:

    def __init__(self, name, age, is_calm = False, is_hungry = False):
        self.name = name
        self.age = age
        self.is_calm = is_calm
        self.is_hungry = is_hungry


child1 = Child('Айгуль', 40)
child2 = Child('Владислав', 23)
child3 = Child('Мирослава', 18)
child4 = Child('Кира', 5)
parent = Parent('Марина', 43, [child1, child2, child3, child4])
parent.feed_child(child1)
parent.feed_child(child3)
parent.calm_down(child2)
parent.calm_down(child4)
parent.feed_child(child4)
parent.say_about_youself()
