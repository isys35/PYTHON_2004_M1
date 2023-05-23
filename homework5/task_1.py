
number_1 = int(input("Введите число от 1 до 12: "))
factor = 1

print(f"Таблица умножения для числа {number_1}:")
while factor <= 10:
    print(f"{number_1} * {factor} = {number_1 * factor}")
    factor += 1