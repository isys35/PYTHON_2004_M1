MAX_PEOPLE = 10
user_input = int(input("Введите количество гостей: "))
guests_count = list(range(0, user_input))
# print(guest_count)

if user_input >= MAX_PEOPLE:
    print("Too many people")
else:
    for guests in guests_count:
        guest_name = str(input("Имя вашего гостя: "))
        print(f"'{guest_name}' has been invited")

# Тут есть вопрос. Rак красиво закончить программу после выполнения цикла?
