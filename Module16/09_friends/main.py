def check(from_p, to_p, money):
    if 0 < from_p <= len(friend_list) and 0 < to_p <= len(friend_list) and from_p != to_p and 0 < money:
        return False
    else:
        print("Неверные данные")
        return True


def transfer(from_p, to_p, money):
    friend_list[from_p - 1][1] -= money
    friend_list[to_p - 1][1] += money


n = int(input("Кол-во друзей: "))
friend_list = []
for i in range(1, n + 1):
    friend_list.append([i, 0])
print(friend_list)
k = int(input("Долговых расписок: "))

for i in range(k):
    flag = True
    while flag:
        print(f"{i + 1} расписка")
        from_person = int(input("Кому: "))
        to_person = int(input("От кого: "))
        count = int(input("Сколько: "))
        flag = check(from_person, to_person, count)
        print()
    transfer(from_person, to_person, count)

print("Баланс друзей:")

for i in range(len(friend_list)):
    print(f"{friend_list[i][0]}: {friend_list[i][1]}")

