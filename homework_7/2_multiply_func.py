# Homework-7: Task-2
"""
Напишите программу с функцией, которая аргументами получает ссылку на функцию и целое число.
Результатом которой является n-кратное исполнение переданной функции
Результатом выполнения задания является подобная функция:
    def get(func, n):
        ...
"""

import random

MARS_WORDS_LIST = ['Mars', 'Red Planet', 'Colonize', 'We', 'Will', 'Martian']


def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return value


def multiply_func(func, quantity):
    for _ in range(quantity):
        func(quantity)


def colonize_mars(n):
    sentence = ' '.join(random.sample(MARS_WORDS_LIST, n))
    print(sentence)


if __name__ == "__main__":
    amount = get_input("Enter the integer value: ")
    print("------------------------------------")
    multiply_func(colonize_mars, amount)
