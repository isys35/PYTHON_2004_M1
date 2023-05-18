try:
    numbers = list(map(int, input("Введите три целочисленных числа через пробел: ").split()))
    if len(numbers) > 3 or len(numbers) < 3:
        print("Невернное количество чисел!")
    else:
        numbers.sort()
        step = numbers[1] - numbers[0]
        if step + numbers[1] == numbers[2]:
            print(True)
        else:
            print(False)
except Exception as e:
    print("Неправильный ввод чисел!")
