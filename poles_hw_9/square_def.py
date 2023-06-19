def square_generate(input):
    for i in range(input):
        yield i ** 2


user_input = int(input('Введите количество элементов: '))

iter_obj = square_generate(user_input)
for n in iter_obj:
    print(n)