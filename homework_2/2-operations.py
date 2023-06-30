# Homework-2: Task-2
"""
Задача 2.
Создайте программу, которая запрашивает у пользователя два целых числа a и b,
после чего выводит на экран результаты следующих математических операций:
- сумма a и b;
- разница между a и b;
- произведение a и b;
- частное от деления a на b;
- остаток от деления a на b;
- результат возведения числа a в степень b.
"""


def get_number(value):
    while True:
        try:
            number = int(input(value))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return number


number_1 = get_number("Input number 1: ")
number_2 = get_number("Input number 2: ")

list_of_operations = [
    f"Addition: {number_1 + number_2}",
    f"Subtraction: {number_1 - number_2}",
    f"Multiplication: {number_1 * number_2}",
    f"Division: {number_1 / number_2:.2f}",
    f"Modulus: {number_1 % number_2}"
]

print(*list_of_operations, sep="\n")
