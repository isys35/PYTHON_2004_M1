
def months():
    month = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
             "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
    for i in month:
        yield i

year = months()
for month in year:
    print(month)