while True:
    result = []
    price = 0
    guest = 0
    sum_ticket = int(input("Введите количество билетов: "))
    for count in range(sum_ticket):
        guest += 1
        age = int(input(f"Введите возраст {guest}-го посетителя: "))
        if age <= 18:
            result.append(0)
        elif age > 18 and age < 25:
            result.append(990)
        elif age >= 25:
            result.append(1390)
    price = int(sum(result))
    if sum_ticket > 3:
        price_discont = price - (price*0.1)
        print(f"\nЦена билетов co скидкой: {price_discont} рублей\n")
    else:
        print(f"\nЦена билетов без скидки: {price} рублей\n")
