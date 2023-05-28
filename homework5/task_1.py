while True:
    try:
        numbers = int(input("Введите число от 1 до 12: "))
        if isinstance(numbers, int) and numbers <= 12 and numbers >= 1:
            factors = range(1, numbers + 1)

            print(f"Таблица умножения для числа {numbers}:")

            for factor in factors:
                print(f"{numbers} * {factor} = {numbers * factor}")
            break
        else: raise ValueError

    except ValueError:
        print("Необходимо ввести число в диапазоне от 1 до 12!")