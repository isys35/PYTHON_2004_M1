while True:
    try:
        triangle = input("Введите желаемые стороны треугольника через ',': ").split(',')

        triangle_1 = int(triangle[0])
        triangle_2 = int(triangle[1])
        triangle_3 = int(triangle[2])

        if isinstance(triangle_1, int) and isinstance(triangle_2, int) and isinstance(triangle_3, int):
            if triangle_1 + triangle_2 > triangle_3 and triangle_1 + triangle_3 > triangle_2 and triangle_2 + triangle_3 > triangle_1:
                print(f"Треугольник со сторонами {triangle} существует.")
            else: print("Создание такого треугольника невозможно!")
            break
        else: raise ValueError
    except ValueError:
        print("Введите стороны треугольника числами!")
        