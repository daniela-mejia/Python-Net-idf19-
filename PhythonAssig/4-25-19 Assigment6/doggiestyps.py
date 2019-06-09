#Daniela Mejia 04/25/2019
#design class pet name

#class
class DogsaretDaBest:

    def __init__(self, name, petType, age):
        self.__name = name
        self.__animal_type = petType
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal(self, petType):
        self.__animal_type = petType

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
#main function to ask user for input and print results
def main()
    doggy = DogsaretDaBest(input("Enter Your Dog's Name: "),"Dog",int(input("Enter Your Dog's Age: ")))

    print(doggy.get_name())
    print(doggy.get_type())
    print(doggy.get_age())


main()
