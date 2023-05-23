
party_people = int(input("Сколько человек вы хотите пригласить на вечеринку? - "))

if party_people < 10:
    while party_people > 0:
        name = input("Введите имя приглашаемого: ")
        print(f"{name} has been invited")
        party_people -= 1
else: print("Too many people")