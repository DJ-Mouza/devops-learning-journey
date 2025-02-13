# Conditional Nested if/ else /elif

# Rollercoaster example
# condition 1 - height must be greater than 120.
# condition 2 - if condition 1 is met check age:
#               if age is under 12 pay $5
#               if age is under 18 pay $7
#               if age is over  18 pay $12



print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?"))

if height > 120:                                                                           
    print("You can ride the rollercoaster")

    age = int(input("What is your age?"))
    if age <= 12:
        print("Please pay $5!")
    elif age <= 18:
        print("Please pay $7")
    elif age <= 25:
        print("Please pay $10")                
    else:
        print("Please pay $12")                                                

else:                                                                                     
    print("Sorry you have to grow taller before you can ride.")    