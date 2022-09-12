print("Hello world\n"*4 + "I love python\n"*4)

month = int(input("Enter a month "))
if month >= 1 and month <= 12 :
    if (month >= 3) and (month <= 5) :
      print("We are on Spring")
    elif(month >= 6) and (month <= 8):
        print("we are in Summer")
    elif(month >= 9) and (month <= 11):
        print("we are in Autumn")
    else:
        print("we are in Winter")