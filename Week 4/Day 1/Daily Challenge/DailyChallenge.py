import random

string =str(input("Enter a string: "))
if len(string) <= 10:
    print("String not too long")
elif len(string) >= 10:
    print("String too long")
else:
    print(string[0], string[len(string)-1])

const = ""
for i in string:
    const = const + i
    print(const)
main = list(string)
random.shuffle(main)
mainstring = "".join(main)
print(mainstring)

