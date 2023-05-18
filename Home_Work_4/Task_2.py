try:
    numbers = list(map(int, input("Введите три целочисленных числа через пробел: ").split()))
    if len(numbers) > 3 or len(numbers) < 3:
        print("Невернное количество чисел!")
    else:
        numbers.sort()
        step = numbers[1] - numbers[0]
        print(True if step + numbers[1] == numbers[2] else False)
except ValueError:
    print("Неправильный ввод чисел!")
