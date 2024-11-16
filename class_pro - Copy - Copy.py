
class Dog:
    attr1 = "cat"
    attr2 = "dog"

    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

animal = Dog()
print(animal.attr1)
animal.fun()
