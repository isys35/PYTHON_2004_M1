class List:
    '''Класс содержащий список чисел'''

    def __init__(self, list):
        '''создаю пустой список, что бы в дальнейшем его наполнить только числами '''
        self.list = []
        for i in list:
            if type(i) == int or type(i) == float:  #проверка для исключения других типов данных
                self.list.append(i)                 #добавление в новый список только численных значений


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


