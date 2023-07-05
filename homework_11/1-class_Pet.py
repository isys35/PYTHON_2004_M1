# Homework-11: Task-1
"""
Напишите класс Pet (Домашнее животное), который должен иметь приведенные ниже атрибут данных:
https://github.com/isys35/PYTHON_2004_M1/issues/46
"""


class Pet:
    def __init__(self, name: str, animal_type: str, age: int):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_animal_type(self, new_animal_type: str):
        self.__animal_type = new_animal_type

    def set_age(self, new_age: int):
        self.__age = new_age

    def get_name(self) -> str:
        return self.__name

    def get_animal_type(self) -> str:
        return self.__animal_type

    def get_age(self) -> int:
        return self.__age


if __name__ == '__main__':
    pet = Pet("", "", 0)

    input_name = input("Enter the pet's name: ")
    pet.set_name(input_name)

    input_animal_type = input("Enter the pet's type: ")
    pet.set_animal_type(input_animal_type)

    while True:
        try:
            input_age = int(input("Enter the pet's age: "))
            pet.set_age(input_age)
            break
        except ValueError:
            print("Error: enter a number.")

    print("Pet's name:", pet.get_name())
    print("Pet's type:", pet.get_animal_type())
    print("Pet's age:", pet.get_age())
