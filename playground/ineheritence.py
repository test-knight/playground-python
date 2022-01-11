class Mammal:
    def walk(self):
        print("Walk")


# Dog inheriting from Mammal
class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    # comment to pass without class attributes
    pass
    # def annoying(self):
    #     print("meow meow")


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
cat.annoying()
# cat.bark()
