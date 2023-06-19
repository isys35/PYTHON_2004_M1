
try:
    user_input = int(input('Введите целое неотрицательное число:'))
    # Создаю список и прибавляю единицу для корректной длины списка по условиям
    user_list = list(range(1, user_input + 1))
    # Создаю второй список( функуию reversed загуглил как способ создания списка в обратном порядке
    user_list_2 = list(reversed(user_list))
    # Эту функцию ZIP я запомнил на занятии потому что она красивая и лаконичнаяprint(f'Словарь созданный на основе двух списков:\n {my_dict}')

    my_dict = dict(zip(user_list, user_list_2))
    print(my_dict)
except ValueError:
   print("Введите именно целочисленное значение, а не строку")







