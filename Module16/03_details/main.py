def count_price_details(name_detail):
    counter_detail = 0
    price_details = 0
    for name, price in shop:  # TODO показал распаковку
        counter_detail += name.count(name_detail)  # todo конечно всегда 1, зачем count?
        if name == name_detail:
            price_details += price
    return counter_detail, price_details


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name = input("Название детали: ")
counter, price = count_price_details(detail_name)
print("Кол-во деталей -", counter)
print("Общая стоимость -", price)

