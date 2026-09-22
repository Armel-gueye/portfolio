# Small object-oriented programming exercise using classes and inheritance

class Human:
    def __init__(self, male, female, child):
        self.male = male
        self.female = female
        self.child = child
        self.age = 0

    def grow(self, added_age):
        self.age += added_age

    def display_age(self):
        print(f"Age: {self.age}")


grand = Human("Madou", "Awa", "Ali")
grand.grow(2)
grand.display_age()


class Animal(Human):
    def __init__(self, male, female, child):
        super().__init__(male, female, child)
        self.size = 0

    def increase_size(self, level):
        self.size += level


animal = Animal("Lion", "Lioness", "Cub")
animal.increase_size(3)
print(f"Animal size: {animal.size}")
