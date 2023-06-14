import random
MARS_BASE = ['Mars', 'Red Planet', 'Colonize', 'Curiosity', 'We', 'Will', 'Martian']


def get_input(tip):
    while True:
        try:
            value = int(input(tip))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return value


def multiply_func(func, quantity):
    for _ in range(quantity):
        func(quantity)


def say_something_about_mars(n):
    sentence = ' '.join(random.sample(MARS_BASE, n))
    print(sentence)


if __name__ == "__main__":
    amount = get_input("Enter the integer value: ")
    print("------------------------------------")
    multiply_func(say_something_about_mars, amount)
