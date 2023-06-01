
CALORIES_FAT = 9
CALORIES_CARBOHYDRATES = 4

def calories_count(fat, carbohydrates):
    return fat * CALORIES_FAT + carbohydrates * CALORIES_CARBOHYDRATES


if __name__ == '__main__':
    while True:
        try:
            fat = float(input("Введите количество жиров в граммах, употребленное за день: "))
            carbohydrates = float(input(("Введите количество углеводов, употребленное за день: ")))
            if isinstance(fat, float) or isinstance(carbohydrates, float):
               print(f"За день вы употребили {calories_count(fat, carbohydrates):,} килокалорий(Ккал)")
               break
            else: raise ValueError
        except ValueError:
            print("Небходимо водить жиры и углеводы числами!")