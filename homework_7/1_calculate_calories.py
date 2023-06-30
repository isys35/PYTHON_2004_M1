# Homework-7: Task-1
"""
Диетолог работает в спортивном клубе и дает рекомендации клиентам в отношении диеты.
В рамках своих рекомендаций он запрашивает у клиентов количество граммов жиров и углеводов,
которые они употребили за день. Затем на основе приведенной ниже формулы он вычисляет количество калорий,
которые получаются в результате употребления жиров:
 -    [калории от жиров = граммы жиров * 9].
Затем на основе еще одной формулы он вычисляет количество калорий,
которые получаются в результате употребления углеводов:
 -    [калории от углеводов = граммы углеводов х 4].
Диетолог просит вас написать программу, которая выполнит эти расчеты.
"""


def get_float_input(tip):
    while True:
        try:
            value = float(input(tip))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return value


def calculate_calories(fat, carb):
    calories_from_fat = fat * 9
    calories_from_carbs = carb * 4
    return f"Calories from fat: {calories_from_fat}" \
           f"\nCalories from carbs: {calories_from_carbs}"


if __name__ == "__main__":
    grease = get_float_input("Enter the number (grams) of grease: ")
    carbs = get_float_input("Enter the number (grams) of carbs: ")

    print(calculate_calories(grease, carbs))
