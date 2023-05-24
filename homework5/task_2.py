
party_people = int(input("Сколько человек вы хотите пригласить на вечеринку? - "))

if party_people < 10:
    while True:
        name = input("Введите имя приглашаемого: ").title()

        if name == "":
            break

        print(f"{name} has been invited")

else: print("Too many people")