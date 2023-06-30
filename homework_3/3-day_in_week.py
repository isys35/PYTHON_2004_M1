# Homework-3: Task-3
"""
Напишите программу, в которой пользователь вводит целое число от 1 до 7 включительно,
а программа выводит название дня недели, соответствующее этому числу
("Понедельник" для 1, "Вторник" для 2, и так далее).
"""

week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

while True:
    try:
        number = int(input("Enter an integer: "))
        print(week.get(number, "This day of the week does not exist."))
    except ValueError:
        print("Invalid input.")
