# Conditional Nested if/else/elif - Rollercoaster Ticket Pricing

# Display a welcome message for the rollercoaster
print("Welcome to the rollercoaster")

# Get the user's height and convert it to an integer
height = int(input("What is your height in cm?"))

# Initialize the bill variable to 0
bill = 0

# Check if the user's height meets the minimum requirement for the rollercoaster
if height >= 120:
    print("You can ride the rollercoaster!")

    # If the height condition is met, ask for the user's age
    age = int(input("What is your age?"))

    # Determine ticket price based on age
    if age <= 12:
        bill = 5  # Child tickets cost $5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7  # Youth tickets cost $7
        print("Youth tickets are $7")
    else:
        bill = 12  # Adult tickets cost $12
        print("Adult tickets are $12")

    # Ask if the user wants a photo taken and add cost if yes
    wants_photo = input("Do you want to have a photo taken? Type 'y' for Yes and 'n' for No: ")
    if wants_photo == "y":
        bill += 3  # Add $3 to the bill for a photo
        print("A photo has been added to your bill for $3")

    # Display the final bill
    print(f"Your final bill is ${bill}")

else:
    # If the height condition is not met, display a message
    print("Sorry, you need to grow taller before you can ride.")
