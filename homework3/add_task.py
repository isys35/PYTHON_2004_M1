while True:
    try:
        feet = float(input("Введите расстояние в футах: "))
        if isinstance(feet, float):
            inch = feet * 12
            yard = feet * 0.333333
            mile = feet * 0.000189394

            print(f"Ваше расстояние в дюймах: {inch:,.0f}, в ярдах: {yard:,.2f}, в милях: {mile:,.2f}")
            break
        else: raise ValueError

    except ValueError:
        print("Введите расстояние числом!")