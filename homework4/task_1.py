
writers = ["Лермонтов", "Гоголь", "Толстой", "Достоевский", "Чехов"]
product = ["Герой нашего времени", "Мертвые души", "Война и мир", "Преступление и наказание", "Вишневый сад"]

dict_test = {writers[index]: product[index] for index in range(len(writers))}

qestions = 0
right = 0
while qestions < len(product):
    answer = input(f"Кто написал прозведение {product[qestions]}? - ").title()
    if answer in writers[qestions]:
        right += 1
    qestions += 1

print(f"Количество верных ответов: {right} из {qestions}")