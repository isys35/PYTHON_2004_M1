# Homework-3: Task-1
"""
Напишите программу, в которой пользователь вводит три числа, а программа определяет,
может ли существовать треугольник со сторонами, длина которых равняется введенным значениям.
Условие существования треугольника такое: сумма двух любых (из трех введенных) чисел должна быть больше третьего числа.
"""

while True:
    try:
        numbers = list(map(int, input("Enter three numbers separated by spaces: ").split()))
        if len(numbers) != 3:
            print("Incorrect number of values entered.")
        else:
            print(True if numbers[0] + numbers[1] > numbers[2] else False)
            break
    except ValueError:
        print("Invalid input of numbers.")
