
compnum = 50
attempts = 0
answer = 0

while compnum != answer:
    try:
        answer = int(input("Введите чисто: "))
        if isinstance(answer, int):
            if answer > compnum:
                print("Ваше число больше необходимого, попробуйте еще")
            elif answer < compnum:
                print("Ваше число меньше необходимого, попробуйте еще")
            attempts += 1
        else: raise ValueError
    except ValueError:
        print("Необходимо ввести число!")

print(f"Well done, you took {attempts} attempts")