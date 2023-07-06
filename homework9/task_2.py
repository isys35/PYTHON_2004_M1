
def quaters(n):
    for i in range(n):
        yield 2 ** (i+1)

input_quaters = int(input("В какую степень возведем двойку? - "))

for i in quaters(input_quaters):
   print(i, end=' ; ')