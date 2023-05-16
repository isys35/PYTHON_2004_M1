payment = int(input("Введите сумму Вашего заказа :"))
tax = payment * 0.04
tip = (payment - tax) * 0.18
total = payment + tip

print("Налог на Ваш заказ равен " + str(tax))
print("В качестве чаевых мы оставим " + str(tip))
print("В итоге Вы заплатите " + str(total))

#коммит zxc

