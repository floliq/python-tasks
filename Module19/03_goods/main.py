goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product, articul in goods.items():
    total_count = 0
    total_price = 0
    for item in store[articul]:
        total_count += item['quantity']
        total_price += item['price'] * item['quantity']
    print('{name} — {count} штук, стоимость {price} рубля'.format(
        name=product,
        count=total_count,
        price=total_price
    ))

