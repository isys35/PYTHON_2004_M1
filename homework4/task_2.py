
len_dict = int(input("Введите целое неотрицетельное число: "))
dict_keys = list(range(1, len_dict + 1))
dict_value = list(reversed(dict_keys))

dict_task = {dict_keys[index]: dict_value[index] for index in range(len(dict_keys))}
print(f"Ваш словарь: {dict_task}")