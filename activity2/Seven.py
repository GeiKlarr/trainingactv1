class Pet:

    def __init__(self,dog_name,dog_breed,dog_color):
        self.dog_name = dog_name
        self.dog_breed = dog_breed
        self.dog_color = dog_color

    def purchasePet(self,dog_name,dog_breed,dog_color):
        print("I bought a " + dog_color + " " + dog_breed + " and I named my dog " + dog_name)

    def purchasePetUsingFormString(self, dog_name, dog_breed, dog_color):
        print("I bought a {} {} and I named my dog {}".format(dog_color,dog_breed,dog_name))

    def run(self):
        print("Your ANIMAL is running")


class Dog(Pet):
    pass



pet = Pet("Max","Labrado","Black")
pet.purchasePet("Max","Labrado","Black")
pet.purchasePetUsingFormString("Max","Labrado","Black")

dog = Dog("MAX","Labrado","Black&White")

pet.dog_name = dog.dog_name

print(pet.dog_name) #Ovve

