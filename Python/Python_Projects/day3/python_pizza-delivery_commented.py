# Python Pizza Order Program
# This program calculates the final bill based on the user's pizza size and preferences for toppings.
# The user selects their pizza size, whether they want pepperoni, and if they'd like extra cheese.

# Welcome message to greet the user
print("Welcome to Python Pizza Deliveries\n")

# Get the pizza size from the user (S for Small, M for Medium, L for Large)
size = input("What size pizza do you want? S, M or L: \n")

# Initialize the bill variable to 0 (this will store the final bill amount)
bill = 0

# Check the selected pizza size and calculate the base price accordingly
if size.lower() == "s":  # If the user selected Small pizza
    print("Your bill is $15")  # Base price for small pizza is $15
    bill = 15  # Set the initial bill to $15
    # Ask the user if they want pepperoni on their pizza
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
    if pepperoni.lower() == "y":  # If the user wants pepperoni
        bill += 2  # Add $2 for pepperoni
        print(f"Your new bill is ${bill}")  # Display updated bill
    else:
        print(f"Your bill is ${bill}")  # If no pepperoni, just display the current bill

elif size.lower() == "m":  # If the user selected Medium pizza
    print("Your bill is $20")  # Base price for medium pizza is $20
    bill = 20  # Set the initial bill to $20
    # Ask the user if they want pepperoni on their pizza
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
    if pepperoni.lower() == "y":  # If the user wants pepperoni
        bill += 3  # Add $3 for pepperoni on medium pizza
        print(f"Your new bill is ${bill}")  # Display updated bill
    else:
        print(f"Your bill is ${bill}")  # If no pepperoni, just display the current bill

elif size.lower() == "l":  # If the user selected Large pizza
    print("Your bill is $25")  # Base price for large pizza is $25
    bill = 25  # Set the initial bill to $25
    # Ask the user if they want pepperoni on their pizza
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n")
    if pepperoni.lower() == "y":  # If the user wants pepperoni
        bill += 3  # Add $3 for pepperoni on large pizza
        print(f"Your new bill is ${bill}")  # Display updated bill
    else:
        print(f"Your bill is ${bill}")  # If no pepperoni, just display the current bill

# Ask the user if they want extra cheese on their pizza
extra_cheese = input("Do you want extra cheese? Y or N: \n")
if extra_cheese.lower() == "y":  # If the user wants extra cheese
    bill += 1  # Add $1 for extra cheese
    print(f"Your final bill is ${bill}")  # Display the final bill with extra cheese
else:
    print(f"Your final bill is ${bill}")  # Display the final bill without extra cheese
