# Homework-3: Task-2
"""
Напишите программу, в которой пользователь вводит три целых числа, а программа проверяет,
являются ли эти числа тремя последовательными элементами арифметической последовательности.
В арифметической последовательности каждый новый член получается прибавлением к предыдущему
определенного фиксированного числа.
"""

while True:
    try:
        numbers = list(map(int, input("Enter three integer numbers separated by space: ").split()))
        if len(numbers) != 3:
            print("Wrong number of values.")
        else:
            numbers.sort()
            step = numbers[1] - numbers[0]
            print(True if step + numbers[1] == numbers[2] else False)
    except ValueError:
        print("Invalid input of numbers.")
