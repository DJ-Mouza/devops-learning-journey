# Request for user to input a number
#convert the number to an interger
#compare if the number is Odd or Even.

user_input = input("What is the number you want to check?\n ")

new_number = int(user_input)

if (new_number) % 2 == 0:
    print("you have typed an Even number")

else:
    print("you have typed an Odd number")    

