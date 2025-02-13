# Conditional Nested if/else/elif - Rollercoaster Ticket Pricing

# Display a welcome message to the user
print("Welcome to the rollercoaster")

# Get the user's height and convert it to an integer
height = int(input("What is your height in cm?"))

# Check if the user's height is greater than or equal to 120 cm (minimum height requirement)
if height >= 120:
    print("You can ride the rollercoaster!")

    # If height is sufficient, ask for the user's age
    age = int(input("What is your age?"))

    # Check the ticket price based on age
    if age <= 12:
        print("Child tickets are $5")  # Child tickets cost $5
    elif age <= 18:
        print("Youth tickets are $7")  # Youth tickets cost $7
    else:
        print("Adult tickets are $12")  # Adult tickets cost $12

else:
    # If the height is less than 120 cm, print a message saying they cannot ride
    print("Sorry, you need to grow taller before you can ride.")
 