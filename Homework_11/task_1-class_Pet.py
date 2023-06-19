class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, new_name):
        self.__name = new_name

    def set_animal_type(self, new_animal_type):
        self.__animal_type = new_animal_type

    def set_age(self, new_age):
        self.__age = new_age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


if __name__ == '__main__':
    pet = Pet("", "", 0)

    name = input("Enter the pet's name: ")
    pet.set_name(name)

    animal_type = input("Enter the pet's type: ")
    pet.set_animal_type(animal_type)

    while True:
        try:
            age = int(input("Enter the pet's age: "))
            pet.set_age(age)
            break
        except ValueError:
            print("Error: enter a number")

    print("Pet's name:", pet.get_name())
    print("Pet's type:", pet.get_animal_type())
    print("Pet's age:", pet.get_age())
