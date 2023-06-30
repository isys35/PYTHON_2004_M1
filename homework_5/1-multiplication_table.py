# Homework-5: Task-1
"""
Предложите пользователю ввести число от 1 до 12. Выведите таблицу умножения для этого числа.
"""

while True:
    try:
        number = int(input("Enter a number between 1 and 12: "))
        if 1 <= number <= 12:
            break
        else:
            print("The number must be between 1 and 12.")
    except ValueError:
        print("Please enter an integer.")

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")
