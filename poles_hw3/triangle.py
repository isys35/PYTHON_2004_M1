# Инициальзируем ввод

print("Длины сторон треугольника")
edge_a = float(input('Введите длину стороны A: ')) # Здесь использую тип данных Float потому, что черепашка попросила как источник
edge_b = float(input('Введите длину стороны B: '))
edge_c = float(input('Введите длину стороны C: '))

if edge_a + edge_b > edge_c and edge_a + edge_c > edge_b and edge_b + edge_c > edge_a:  # Логическое условие существование треугольника
    print("Треугольник возможно построить.")

    import turtle # Рисуем результат черепашкой

    turtle.setup(1000, 1000, 0, 0)
    turtle.penup()
    turtle.begin_fill()
    turtle.goto(0, edge_a * 10)
    turtle.goto(edge_b * 10, 7)
    turtle.goto(0, 0)
    turtle.end_fill()

    turtle.done()

else:
    print("Треугольник не может существовать.") # Иначе

import turtle

