
while True:
    try:
        party_people = int(input("Сколько человек вы хотите пригласить на вечеринку? - "))
        if isinstance(party_people, int):
            if party_people < 10:
                while True:
                    name = input("Введите имя приглашаемого(Enter для выхода): ").title()

                    if not name:
                        break

                    print(f"{name} has been invited")
            else:
                print("Too many people")
            break

        else: raise ValueError

    except ValueError:
        print("Введите количество человек числом!")
