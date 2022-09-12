number = int(input('Please state a number between 1 and 100: '))

if number >= 1 and number <= 100 :
    if (number % 3 == 0) and (number % 5) == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
else:
    print("Try again")
