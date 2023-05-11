summa_zakaza = int(input('Enter your burger price : '))

tips = (summa_zakaza*18) / 100
print('Tips :', tips)

tax = (summa_zakaza * 4) / 100
print('Tax :', tax)

total = (summa_zakaza + tips+ tax)
print('Total :', total)

print("Thank you, come again")

