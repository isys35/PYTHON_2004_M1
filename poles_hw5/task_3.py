compnum = 50
running = True

counter = 0  # Долго не получалось правильно вставить счетчик в цикл
while running:

    user_input = int(input("Введите число : "))

    if user_input == compnum:
        print("Вы угадали число")
        running = False
        counter += 1
    if user_input < compnum:
        print("Введенное число меньше заданного")
        counter += 1 
    if user_input > compnum:
        print("Введенное число больше заданного")
        counter += 1
else:
    print(f"Количество попыток : {counter}")
