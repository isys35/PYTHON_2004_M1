number_1, number_2 = int(input("Input number 1: ")), int(input("Input number 2: "))

list_of_operations = [
    number_1 + number_2,
    number_1 - number_2,
    number_1 * number_2,
    number_1 / number_2,
    number_1 % number_2
    ]

print(*list_of_operations, sep='\n')
