print(3 <= 3 < 9)
print(3 == 3 == 3)
print(bool(0))
print(bool(5 == "5"))
print(bool(4 == 4) == bool("4" == "4"))
print(bool(bool(None)))

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamcolaboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

sentence = input("The longest sentence you can without the A ")
if "A" in sentence:
    print('Try again')
else:
    print("Congratulation")
