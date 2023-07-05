# Homework-13: Task-1
"""
Напишите программу с абстрактным классом Country. Опишите наследуемые от класса Country классы Russia, Canada, Germany.
Добавьте поле population и добавьте геттер и сеттер для этого поля.
"""


class Country:
    def __init__(self, population):
        self._population = population

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value


class Russia(Country):
    pass


class Canada(Country):
    pass


class Germany(Country):
    pass


if __name__ == '__main__':
    print(Germany(34553).population)
