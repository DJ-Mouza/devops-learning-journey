
# Rollercoaster Height Check - Conditional Statements Tutorial

# Display a welcome message to the user
print("Welcome to the rollercoaster!")

# Ask the user for their height and convert the input to an integer
height = int(input("What is your height in cm?"))

# Check if the user's height is greater than 120 cm (minimum height requirement)
if height > 120:  # If the condition is true (height > 120)
    print("You can ride the rollercoaster")  # Execute this line if the condition is met

else:  # If the condition is not met (height <= 120)
    print("Sorry, you have to grow taller before you can ride.")  # Execute this line if the condition is not met