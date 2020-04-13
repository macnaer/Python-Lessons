
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        print("Constructor Working...")

    def __del__(self):
        print("Desctructor working...")

    def person_info(self):
        print(self.__name, " <-> ", self.__age, " years old")

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if self.__age == new_age:
            print("The same age")
        else:
            self.__age = new_age


bill = Person("Billy", 56)
print("Bill age before => ", bill.name)
print("Bill age before => ", bill.age)
bill.age = 58
# bill.name = "Test" Error
print("Bill age after => ", bill.name)
print("Bill age after => ", bill.age)

# bill.person_info()

# print(bill.get_name())
# print("Before +> ", bill.get_age())
# bill.set_age(70)
# print("After +> ", bill.get_age())

# stive = Person("Stiven", 26)
# stive.person_info()
