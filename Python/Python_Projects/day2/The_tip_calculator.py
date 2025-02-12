# Welcome to the tip calculator!
# What was the total bill?
# How much tip would you like to give? 10,12, or 15?
# How many people to split the bill?
# Each person should pay:

print("Welcome to the tip calculator!\n")

total_bill = input("What was the total bill?")

print(f"${total_bill}\n")                                                                               # print total_bill in $ on the next line

tip = input("How much tip would you like to give? 10,12, or 15?")

print(f"{tip}%\n")                                                                                       # print tip in % on the next line

number_of_people = input("How many people to split the bill?")

print(f"{number_of_people} people\n")                                                                    # print the number of people on the next line

new_total_bill = float(total_bill)                                                                       # convert total_bill from 'string' to float
new_tip = int(tip)                                                                                       # convert tip from 'string' to int
new_number_of_people = int(number_of_people)                                                             # convert number of people from 'string' to int

bill_split = ((new_total_bill) + ((new_total_bill) * (new_tip)/100))/(new_number_of_people)

new_bill_split = (round(bill_split, 2))                                                                  # Round up the bill_split to two decimal places

print(f"Each person should pay:${new_bill_split}")                                                       # print new_bill_split in $ using f-string



