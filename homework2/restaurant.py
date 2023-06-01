
while True:
    try:
        payment = int(input("Введите сумму Вашего заказа :"))
        if isinstance(payment, int):
            tax = payment * 0.04
            tip = (payment - tax) * 0.18
            total = payment + tip

            print(f"Налог на Ваш заказ равен {tax:.2f}")
            print(f"В качестве чаевых мы оставим {tip:.2f}")
            print(f"В итоге Вы заплатите {total:.2f}")
            break
        else: raise ValueError

    except ValueError:
        print("Введите действительную сумму!")