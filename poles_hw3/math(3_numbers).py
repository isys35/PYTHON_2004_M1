#Инициализируем ввод данных


num_a = int(input('Число 1: '))
num_b = int(input('Число 2: '))
num_c = int(input('Число 3: '))

# Условие при котором каждый элемент меньше предыдущего на разницу между членами последовательности
if num_b - num_a == num_c - num_b:
    print("Являются тремя последовательными элементами")
else:
    print("Не являются тремя последовательными элементами")

