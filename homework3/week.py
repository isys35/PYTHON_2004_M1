day_nomber = input("Введите чисто дня недели: ")

match day_nomber:
    case "1":
        print("Понедельник")
    case "2":
        print("Вторник")
    case "3":
        print("Среда")
    case "4":
        print("Четверг")
    case "5":
        print("Пятница")
    case "6":
        print("Суббота")
    case "7":
        print("Воскресенье")
    case _:
        print("Неверный день недели")
