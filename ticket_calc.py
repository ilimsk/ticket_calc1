
while True:
    z = []
    price = None
    sum_ticket = int(input("Введите количество билетов: "))
    for count in range(sum_ticket):
        age = int(input("Введите возраст: "))
        if age <= 18:
            z.append(0)
        elif age > 18 and age < 25:
            z.append(990)
        elif age >= 25:
            z.append(1390)
    if sum_ticket >= 3:
        price = int(sum(z))-(int(sum(z))*0,1)
        print(f"\nЦена билетов co скидкой: {price} рублей")
    else:
        price = sum(z)
        print(f"\nЦена билетов без скидки: {price} рублей")