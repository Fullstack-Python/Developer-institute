class Zoo():

# 2. In this class create a method __init__ that takes one parameter: zoo_name. It instantiates two attributes: animals (an empty list) and name (name of the zoo).
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = ["putois", "chevre", "singe", "Antiloppe"]

# 3. Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.

    def add_animal(self, new_animal):
        while new_animal not in self.animals:
            self.animals.append(f"Add_animal: {new_animal}")
        else:
            self.animals.append(f"Add_animal: {new_animal}")


# 4. Create a method called get_animals that prints all the animals of the zoo.

    def get_animals(self):
        print(self.animals)

# 5. Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.

    def sell_animal(self, animal_sold):
        if animal_sold <= 0:
            print(f"{self.animals} is empty")
        elif animal_sold >= 0:
            animal_sold -= self.animals

# 6. Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.

    def sort_animals(self):
        for animals in self.animals:
            sorted(self.animals)




