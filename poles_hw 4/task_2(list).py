user_input = int(input('Введите целое неотрицательное число:'))
# Создаю список
user_list = list(range(1, user_input))
# Создаю второй список( функуию reversed загуглил как способ создания списка в обратном порядке
user_list_2 = list(reversed(user_list))

# Эту функцию ZIP я запомнил на занятии потому что она красивая и лаконичная
my_dict = dict(zip(user_list, user_list_2))
print(f'Словарь созданный на основе двух списков:\n {my_dict}')
