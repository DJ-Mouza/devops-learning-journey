# Request for user to input a number
#convert the number to an interger
#compare if the number is Odd or Even.

# Python Tutorial: Checking if a Number is Odd or Even

# Prompt the user to input a number
user_input = input("What is the number you want to check?\n")

# Convert the user input (which is a string) to an integer
new_number = int(user_input)

# Check if the number is even (i.e., divisible by 2 with no remainder)
if new_number % 2 == 0:
    print("You have typed an Even number")  # If the number is divisible by 2, it's even
else:
    print("You have typed an Odd number")   # Otherwise, the number is odd
