while True:
    try:
        number = int(input("Введите положительное целочисленное число: "))
        if number < 0:
            raise ValueError
        break
    except ValueError:
        print("Неверный Ввод. Пожалуйста, введите неотрицательное целое число.")

lst = list(range(1, number + 1))
dct = {i: lst[-i] for i in lst}
print(dct)
