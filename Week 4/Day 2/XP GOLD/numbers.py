# numbers = 1
# while numbers <= 10:
#     print(numbers)
#     numbers += 1
# print("finished")
import random
win = "Winner"
lose = "Better Luck Next Time"
while True:
 number = int(input("Enter a number "))
 if 0 < number < 10:
  rand = random.randint(1, 9)
  print(rand)
 if number == rand:
  print(win)
 else:
  print(lose)
 x = win.count()
 print(x)
 y = lose.count()
 print(y)



