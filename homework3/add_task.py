
feet = float(input("Введите расстояние в футах: "))

inch = feet * 12
yard = feet * 0.333333
mile = feet * 0.000189394

print(f"Ваше расстояние в дюймах: {inch:,.0f}, в ярдах: {yard:,.2f}, в милях: {mile:,.2f}")