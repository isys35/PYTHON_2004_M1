order_amount = int(input("Введите сумму заказа: "))

tax = order_amount * 4 / 100

new_amount = round(order_amount - tax, 2)

tips = round(new_amount * 18 / 100, 2)

result = round(new_amount - tips, 2)

print(f"Налог - {tax}, Чаевые - {tips}, Прибыль - {result}")
