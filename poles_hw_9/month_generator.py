def month_generator():
    month = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
              'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    for i in month:
        yield 'Current month: ' + i


year = month_generator()
for month in year:
    print(month)