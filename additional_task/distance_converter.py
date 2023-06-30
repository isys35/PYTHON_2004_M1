# Дополнительное задание
"""
Для этого упражнения вам необходимо будет написать программу,
которая будет запрашивать у пользователя расстояние в футах.
После этого она должна будет пересчитать это число в дюймы, ярды и мили и вывести на экран.
Коэффициенты для пересчета единиц вы без труда найдете в интернете.
"""

while True:
    try:
        distant_feet = float(input("Enter the distance in feet: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

distance_data = (
    f"Inches: {distant_feet * 12}",
    f"Yards: {distant_feet * 0.33333:.2f}",
    f"Miles: {distant_feet * 0.00018939:.2f}",
)

print(*distance_data, sep="\n")
