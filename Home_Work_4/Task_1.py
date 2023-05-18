try:
    numbers = list(map(int, input("Введите три целочисленных числа через пробел: ").split()))
    if len(numbers) > 3 or len(numbers) < 3:
        print("Невернное количество чисел!")
    else:
        print(True if numbers[0] + numbers[1] > numbers[2] else False)
except ValueError:
    print("Неправильный ввод чисел!")
