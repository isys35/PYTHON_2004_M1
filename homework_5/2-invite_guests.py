# Homework-5: Task-2
"""
Спросите у пользователя, скольких людей он хочет пригласить на вечеринку.
Если будет введено число меньше 10, запросите имена и после каждого имени выведите строку «[имя] has been invited».
Если введенное число больше или равно 10, выведите сообщение «Too many people».
"""

while True:
    number = int(input("Enter the number of visitors (max 9): "))
    if number <= 9:
        break
    print("Too many people.")

stop_counter = 0
while stop_counter != number:
    visitor = input("Enter name: ")
    stop_counter += 1
    print(f"{visitor} has been invited. {stop_counter}")
else:
    print("Ready!")
