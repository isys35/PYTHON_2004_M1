number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

sum_numbers = number_1 + number_2
minus_number = number_1 - number_2
multiplication_number = number_1 * number_2
separation_numbers = number_1 // number_2
remainder = number_1 % number_2
degree = number_1 ** number_2

print("Сумма ваших числел равна " + str(sum_numbers))
print("Их разница равна " + str(minus_number))
print("Произведение этих числел " + str(multiplication_number))
print("Частное от деления  " + str(separation_numbers))
print("Остаток от деления " + str(remainder))
print("Результат возведения числа " + str(number_1) + " в степень " + str(number_2) + " равен " + str(degree))