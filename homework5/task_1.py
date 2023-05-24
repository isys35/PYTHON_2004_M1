
numbers = int(input("Введите число от 1 до 12: "))
factors = range(1, numbers + 1)

print(f"Таблица умножения для числа {numbers}:")

for factor in factors:
    print(f"{numbers} * {factor} = {numbers * factor}")