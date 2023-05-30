while True:
    try:
        order_numbers = input("Введите желаемые числа через ',': ").split(',')
        if len(order_numbers) != 3:
            raise ValueError
        order_numbers.sort()

        number_1 = int(order_numbers[0])
        number_2 = int(order_numbers[1])
        number_3 = int(order_numbers[2])

        if isinstance(number_1, int) and isinstance(number_2, int) and isinstance(number_3, int):

            step_1 = number_3 - number_2
            step_2 = number_2 - number_1

            if step_1 == step_2:
                print(f"Данные числа: {order_numbers} являются членами арифметической прогрессии.")
            else:
                print(f"Данные числа: {order_numbers} не являются членами арифметической прогрессии.")
            break
        else: ValueError

    except ValueError:
        print("Введите 3 числа!")