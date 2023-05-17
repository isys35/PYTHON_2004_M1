
triangle = input("Введите желаемые стороны треугольника через ',': ").split(',')

triangle_1 = int(triangle[0])
triangle_2 = int(triangle[1])
triangle_3 = int(triangle[2])

if triangle_1 + triangle_2 > triangle_3 and triangle_1 + triangle_3 > triangle_2 and triangle_2 + triangle_3 > triangle_1:
    print(f"Треугольник со сторонами {triangle} существует.")
else: print("Ошибка! Создание такого треугольника невозможно!")