class List:
    '''Класс содержащий список чисел'''

    def __init__(self, list):
        self.list = []
        for i in list:
            if type(i) == int or type(i) == float:
                self.list.append(i)


    def list_showing(self):
        '''метод для отображения созданного списка'''
        return print(self.list)

    def medium_calculation(self):
        '''метод для отображения среднего значения списка элементов'''
        return print(round(sum(self.list) / len(self.list)))


if __name__ == '__main__':
    def main():
        user_list = ['Str', 10, 5, 22.0]
        my_numbers = List(user_list)
        my_numbers.list_showing()
        my_numbers.medium_calculation()

main()


