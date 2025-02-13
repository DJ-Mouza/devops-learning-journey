
# Python Tutorial: Rollercoaster Ticket Price Calculator

# Rollercoaster example
# condition 1 - height must be greater than 120.
# condition 2 - if condition 1 is met check age:
#               if age is under 12 pay $5
#               if age is under 18 pay $7
#               if age is over  18 pay $12
# condition 3 - if want photo add additional cost


# Initial welcome message to the user
print("Welcome to the rollercoaster!")

# Prompt the user to input their height in centimeters
height = int(input("What is your height in cm?"))
# Initialize the bill variable to 0
bill = 0

# Check if the user meets the minimum height requirement
if height >= 120:
    print("You can ride the rollercoaster")  # Display if the user can ride
    
    # Ask for the user's age to determine ticket pricing
    age = int(input("What is your age?"))
    
    # Check the age and set the appropriate ticket price
    if age <= 12:
        bill = 5  # Child ticket price
        print("Child tickets are $5")

    elif age <= 18:
        bill = 7  # Youth ticket price
        print("Youth tickets are $7")

    else:
        bill = 12  # Adult ticket price
        print("Adult tickets are $12")

    # Ask if the user wants a photo taken
    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    
    # If the user wants a photo, add $3 to their bill
    if wants_photo == "y":
        bill += 3  # Add the photo cost

    # Display the final bill
    print(f"Your final bill is ${bill}")

else:
    # Display a message if the user doesn't meet the height requirement
    print("Sorry, you have to grow taller before you can ride")
