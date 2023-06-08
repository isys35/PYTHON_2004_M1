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


if __name__ == '__main__':
    grease = get_float_input("Enter the number (grams) of grease: ")
    carbs = get_float_input("Enter the number (grams) of carbs: ")

    print(calculate_calories(grease, carbs))
