class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bar(self):
        print("bark")


class cat(Mammal):
    pass

dog1 = Dog()
dog1.bark()
