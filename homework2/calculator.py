while True:
    try:
        number_1 = int(input("Введите первое число: "))
        number_2 = int(input("Введите второе число: "))

        if isinstance(number_1, int) and isinstance(number_2, int):
            sum_numbers = number_1 + number_2
            minus_number = number_1 - number_2
            multiplication_number = number_1 * number_2
            separation_numbers = number_1 // number_2
            remainder = number_1 % number_2
            degree = number_1 ** number_2

            print(f"Сумма ваших числел равна {sum_numbers}")
            print(f"Их разница равна {minus_number}")
            print(f"Произведение этих числел {multiplication_number}")
            print(f"Частное от деления {separation_numbers}")
            print(f"Остаток от деления {remainder}")
            print(f"Результат возведения числа {number_1} в степень {number_2} равен {degree:,}")
            break
        else: raise ValueError

    except ValueError:
        print("Ошибка! Введите числа!")