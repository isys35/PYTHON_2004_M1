# Задача номер 1
import math
print('Введите три числа')
a = float(input('Первое число:'))
b = float(input('Второе число:'))
c = float(input('Третье число'))
if 2 * max(a, b, c) > a + b + c:
 print("Треугольник может существовать")
else:
 print("Треугольник не может существоввать")
