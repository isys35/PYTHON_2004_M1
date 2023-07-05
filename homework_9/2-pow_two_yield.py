# Homework-9: Task-2
"""
Напишите программу, в которой используется функция-генератор,
создающая итерируемый объект со степенями двойки.
Количество элементов определяется аргументом функции-генератора.
"""


def pow_two_generate(amount):
    for n in range(amount):
        yield 2 ** n


if __name__ == '__main__':
    while True:
        try:
            numbers_of_pow = int(input("Enter the integer value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    new_elements = pow_two_generate(numbers_of_pow)
    for element in new_elements:
        print(element)
