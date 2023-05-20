number = int(input("Введите целое неотрицательное число:"))
#создаём список натуральных чисел
list_of_numbers = list(range(1, number +1))
#создаём словарь
dictionary ={}
for i in list_of_numbers:
    dictionary[i] = number-i +1
    print(dictionary)