# Python Tutorial: Tip Calculator
# Welcome to the tip calculator!
# What was the total bill?
# How much tip would you like to give? 10,12, or 15?
# How many people to split the bill?
# Each person should pay:

# Welcome message to the user
print("Welcome to the tip calculator!\n")

# Prompt the user to input the total bill amount
total_bill = input("What was the total bill? ")

# Display the total bill in dollars
print(f"${total_bill}\n")

# Prompt the user to choose the tip percentage (10%, 12%, or 15%)
tip = input("How much tip would you like to give? 10, 12, or 15? ")

# Display the selected tip percentage
print(f"{tip}%\n")

# Prompt the user to input the number of people to split the bill
number_of_people = input("How many people to split the bill? ")

# Display the number of people splitting the bill
print(f"{number_of_people} people\n")

# Convert the input values to the appropriate data types:
# total_bill to float, tip to integer, and number_of_people to integer
new_total_bill = float(total_bill)             # Convert total_bill to float
new_tip = int(tip)                             # Convert tip to integer
new_number_of_people = int(number_of_people)   # Convert number_of_people to integer

# Calculate the total bill including the tip, and then split it among the people
bill_split = ((new_total_bill) + ((new_total_bill) * (new_tip) / 100)) / new_number_of_people

# Round the result to two decimal places for clarity
new_bill_split = round(bill_split, 2)

# Display the final amount each person should pay
print(f"Each person should pay: ${new_bill_split}")




