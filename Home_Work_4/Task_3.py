week_base = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}

try:
    number = int(input("Введите целочисленное число: "))
    print(week_base.get(number, "Такого дня недели не существует!"))
except ValueError:
    print("Неправильный ввод!")
