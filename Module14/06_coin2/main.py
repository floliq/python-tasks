import math


def check(x, y, r):
    if math.sqrt(x ** 2 + y ** 2) <= r:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")


x = float(input("Введите x: "))
y = float(input("Введите y:"))
r = float(input("Введите радиус: "))
check(x, y, r)

