class person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("talk")
        levi = person(f"HI I am {self.name}")


print("talk")
print(levi.name)
levi.talk()
