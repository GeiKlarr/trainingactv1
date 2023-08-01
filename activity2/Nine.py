class Person:

    def sing(self):
        return "Sang an unrecognized song "

class Clark(Person):
    def sing(self):
        return super().sing() + "Mi mi yah 🎵🎵"


person = Person()
print(person.sing())

clark = Clark()
print(clark.sing())