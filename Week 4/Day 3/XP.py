        # Exercice 1

# convert two list into a dictionnary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

keys_dictionnary = dict(zip(keys,values))
print(keys_dictionnary)

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

        # Exercice 2

# Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# How much does each family member have to pay ?
for key, value in family.items():
    if value < 3:
        price1 = 0
        print("The ticket for " + key ,"is" ,price1,"$" )
    elif 3 < value <12:
        price2 = 10
        print("The ticket for " + key ,"is" ,price2,"$")
    else:
        price3 = 15
        print("The ticket for " + key ,"is" ,price3,"$")
# print(price1+price2+price3)
# Print out the family’s total cost for the movies.

# Bonus: Ask the user to input the names and ages instead of using the provided
# family variable (Hint: ask the user for names and ages and add them into a
# family dictionary that is initially empty).

junior = {}

x = input("name ")
y = int(input("age "))

junior[x] = y
print(junior)

        # Exercice 3


# Create a dictionary called brand which value is the information from part one
# (turn the info into keys and values).

brand = {}

keys = ["name", "creation_date", "creator_name", "type_of_clothes", "international_competitors", "number_stores", "major_color", "France", "Spain", "US"]
print(key)
values = ["zara", "1975", "Amancio Ortega Gaona", ("men", "women", "children", "home"), ("Gap", "H&M", "Benetton"), 7000, " ", "blue", "red", ("pink" , "green")]
print(value)
brand = dict(zip(keys, values))
print(brand)

# Change the number of stores to 2.

brand["number_stores"] = 2
print(brand)

print("Hello my name is " + brand["name"] + " i create this in " + brand["creation_date"] + " with the institutor " + brand["creator_name"])

brand["country_creation"] = brand["Spain"]
print(brand)

if "international_competitors" in brand:
    brand["international_competitors"] = ("Gap", "H&M", "Benetton", "Desigual")
    print(brand)
del brand["creation_date"]
print(brand)

print(brand["international_competitors"][3])

print(brand["US"])

print(len(brand))

for key, value in brand.items():
    print(key)

more_on_zara = {}

key = ["creation_date", "number_stores"]
value = [1975, 10000]

more_on_zara = dict(zip(key, value))
print(more_on_zara)

brand.update(more_on_zara)
print(brand)

print(brand["number_stores"])

            # Exercise 4 : Disney Characters

users=["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {item: "" for item in enumerate(users)}
print(sorted(disney_users_A))
