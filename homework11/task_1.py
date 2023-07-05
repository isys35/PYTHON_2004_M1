
class Pet:
    def __init__(self, name: str, animal_type: str, age: int):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, new_name):
        self.__name = new_name

    def set_animal_type(self, new_type):
        self.__animal_type = new_type

    def set_age(self, new_age):
        self.__age = new_age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self) -> int:
        return self.__age

def main():
    pet = Pet("", "", 0)

    set_new_name = input("Введите кличку питомца: ")
    pet.set_name(set_new_name)

    set_new_type = input("Введите тип домашнего животного: ")
    pet.set_animal_type(set_new_type)

    while True:
        try:
            set_new_age = int(input("Введите возраст питомца: "))
            pet.set_age(set_new_age)
            break
        except ValueError:
            print("Введите числовое значение!")


    print(f"Кличка: {pet.get_name()}\nТип: {pet.get_animal_type()}\nВозраст: {pet.get_age()}")


if __name__ == "__main__":
    main()
