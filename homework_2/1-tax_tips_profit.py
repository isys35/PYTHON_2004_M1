# Homework-2: Task-1
"""
Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане.
После этого должен быть произведен расчет налога и чаевых официанту.
В качестве чаевых мы оставим 18 % от стоимости заказа без учета налога.
Налог: 4%. На выходе программа должна отобразить отдельно налог, сумму чаевых и итог.
"""

while True:
    try:
        order_amount = float(input("Enter order amount: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid value.")

tax = order_amount * 4 / 100
new_amount = order_amount - tax
tips = new_amount * 18 / 100
profit = new_amount - tips

print(f"Tax - {tax:.2f}, Tips - {tips:.2f}, Profit - {profit:.2f}")
