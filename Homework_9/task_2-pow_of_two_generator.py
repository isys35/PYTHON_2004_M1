def pow_two_generate(amount):
    for n in range(amount):
        yield 2 ** n


numbers_of_pow = int(input())

new_elements = pow_two_generate(numbers_of_pow)
for element in new_elements:
    print(element)
