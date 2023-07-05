# Homework-11: Task-1
"""
Напишите программу, в которой описан класс. У объектов класса должно быть поле, представляющее собой числовой список.
Этот список формируется на основе списка, переданного конструктору в качестве аргумента.
При этом из списка-аргумента в список-поле включаются только числовые элементы (элементы других типов игнорируются).
Необходимо также описать метод, отображающий содержимое поля списка, а также метод,
вычисляющий среднее значение элементов поля списка (сумма значений элементов, деленная на их количество).
"""


class Numbers:
    def __init__(self, data: list):
        self.data = [x for x in data if isinstance(x, int) or isinstance(x, float)]

    def calculate_average(self) -> float:
        return sum(self.data) / len(self.data)

    def show_data(self) -> list:
        return self.data


def check_data_list(input_data):
    if isinstance(input_data, list):
        return input_data
    return print("Wrong data!")


if __name__ == '__main__':
    some_data = [3, 3.2, "soma", '2', 4]    # 123131, {}, (1, 2, 3)

    if check_data_list(some_data):
        new_numbers = Numbers(some_data)
        print(new_numbers.calculate_average())
        print(new_numbers.show_data())
