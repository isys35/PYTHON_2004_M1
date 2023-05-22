
dict_test = {
    "Лермонтов": "Герой нашего времени",
    "Гоголь": "Мертвые души",
    "Толстой": "Война и мир",
    "Достоевский": "Преступление и наказание",
    "Чехов": "Вишневый сад"
}

#пробовал много вариантов перебора самого словаря, но в лучшем случае засчитывал ответ,
#просто находящегося ключа в словаре, но с неверным ответом


writers = list(dict_test.keys())
product = list(dict_test.values())

right = 0
qestions = 0

while qestions < len(product):
    answer = input(f"Кто написал произведение {product[qestions]}? - ").title()
    if answer in writers[qestions]:
        right +=1
    qestions +=1

print(f"Правильных ответов: {right} из {qestions}")