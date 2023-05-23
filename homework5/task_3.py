
compnum = 50
attempts = 0
answer = 0

while compnum != answer:
    answer = int(input("Введите чисто: "))
    if answer > compnum:
        print("Ваше число больше необходимого, попробуйте еще")
    elif answer < compnum:
        print("Ваше число меньше необходимого, попробуйте еще")
    attempts += 1

print(f"Well done, you took {attempts} attempts")