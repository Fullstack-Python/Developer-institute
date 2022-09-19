class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def instance(self):
        print("I am ", self.name ," i have " ,self.age ,"years old")


# 1- Instanciez trois Cat objets à l'aide du code fourni ci-dessus.

cat1 = Cat("mbongo", "2")
cat2 = Cat("didouch", "3")
cat3 = Cat("viky", "1")

# 2- En dehors de la classe, créez une fonction qui trouve le chat le plus ancien et renvoie le chat.

def oldest():
        if cat1.age > cat2.age and cat1.age > cat3.age:
            print(f"The oldest cat is: {cat1.name} and he has {cat1.age} years old")
        elif cat2.age > cat1.age and cat2.age > cat3.age:
            print(f"The oldest cat is: {cat2.name} and he has {cat2.age} years old")
        elif cat3.age > cat1.age and cat3.age > cat2.age:
            print(f"The oldest cat is: {cat3.name} and he has {cat3.age} years old")
oldest()

# Imprimez la chaîne suivante : "Le chat le plus âgé est <cat_name>, et a <cat_age>ans.". Utilisez la fonction précédemment créée.



