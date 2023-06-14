class Numbers:
    def __init__(self, data):
        self.data = [x for x in data if isinstance(x, int) or isinstance(x, float)]

    def calculate_average(self):
        return print(sum(self.data) / len(self.data))

    def show_data(self):
        return print(self.data)


def check_data_list(input_data):
    if isinstance(input_data, list):
        return input_data
    return print("Wrong data!")


if __name__ == '__main__':
    some_data = [3, 3.2, "soma", '2', 4]    # 123131, {}, (1, 2, 3)

    if check_data_list(some_data):
        new_numbers = Numbers(some_data)
        new_numbers.calculate_average()
        new_numbers.show_data()
