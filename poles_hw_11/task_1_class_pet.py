class Pet:
    '''Описание класса питомец'''
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def set_name(self,name):
         self.name = name

    def set_animal_type(self,type):
         self.type = type
         self.animal_type = self.type
         return self.animal_type
    def set_age(self,age):
        self.age = age
        return self.age

    def get_name(self):
        return f' "{self.name}" Очень Вам рад'
    def get_animal_type(self):
        return f' По своей сути Ваш питомец -  {self.animal_type}'

    def get_age(self):
        return f' Вашему питомцу {self.age} года(лет)'

if __name__ == '__main__':
    def main():
        user_input_name = input("Введите кличку Вашего питомца: ")
        user_input_type = input("Введите тип питомца(Котик, Собака, Черепашка и т.д.: ")
        user_input_age = int(input("Введите возраст вашего питомца"))
        mypet = Pet(user_input_name, user_input_type, user_input_age)
        mypet.set_name(user_input_name)
        mypet.set_animal_type(user_input_type)
        mypet.set_age(user_input_age)
        print("Личная карточка Вашего питомца\n"
              "______________________________")
        print(mypet.get_name())
        print(mypet.get_animal_type())
        print(mypet.get_age())

main()

