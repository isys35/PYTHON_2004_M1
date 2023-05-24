compnum = 50

counter = 0  # Долго не получалось правильно вставить счетчик в цикл
while True:

    user_input = int(input("Введите число : "))

    if user_input == compnum:
        print("Вы угадали число")
        running = False
        counter += 1
        break
    if user_input < compnum:
        print("Введенное число меньше заданного")
        counter += 1 
    if user_input > compnum:
        print("Введенное число больше заданного")
        counter += 1

print(f"Количество попыток : {counter}")
