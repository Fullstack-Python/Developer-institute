import time
# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))

# Step 2: Then ask the user to input the length of the countdown in seconds.
# Step 3: This value is sent as a parameter ‘t’ to the user-defined function countdown(). Any variable read using the input function is a string. So, convert this parameter to ‘int’ as it is of string type.
# Step 4: In this function, a while loop runs until time becomes 0.
# Step 5: The divmod() is to calculate the number of minutes and seconds. You can read more about it here.
# Step 6: Now print the minutes and seconds on the screen using the variable timeformat.
# Step 7: Using end = ‘\r’ we force the cursor to go back to the start of the screen (carriage return) so that the next line printed will overwrite the previous one.
# Step 8: The time.sleep() is used to make the code wait for one sec.
# Step 9: Now decrement time so that the while loop can converge.
# Step 10: After the completion of the loop, we will print “Fire in the hole” to signify the end of the countdown.