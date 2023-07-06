# Homework-9: Task-1
"""
Напишите программу, в которой используется функция-генератор,
создающая итерируемый объект с названиями месяцев.
"""


def month_generate():
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December')
    for m in months:
        yield m


new_months = month_generate()
for month in new_months:
    print(month)
