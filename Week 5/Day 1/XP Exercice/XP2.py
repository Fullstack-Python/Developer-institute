class Dog():
    def __init__(self, name,height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} va woof!")

    def jump(self):
        print(f"{self.name} saute {self.height*2}" ,"cm")

davids_dog = Dog("Rex", 50)
print(f"Le chien de davids_dog s'appel {davids_dog.name} et il as une taille de {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Le chien de davids_dog s'appel {sarahs_dog.name} et il as une taille de {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print(f"The biggest dogs is {sarahs_dog.name}")
else:
    print(f"The biggest dogs is {davids_dog.name}")
