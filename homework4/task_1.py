
dict_test = {
    "Лермонтов": "Герой нашего времени",
    "Гоголь": "Мертвые души",
    "Толстой": "Война и мир",
    "Достоевский": "Преступление и наказание",
    "Чехов": "Вишневый сад"
}

right = 0
for writers, product in dict_test.items():
    answer = input(f"Кто написал произведение {product}? - ").title()
    if answer == writers:
        right += 1
    else: right = right
print(f"Правильных ответов: {right}")