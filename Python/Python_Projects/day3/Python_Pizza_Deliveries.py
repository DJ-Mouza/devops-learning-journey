# Python Pizza order program
# based on user's order, work out their final bill.
# Use the input() function to get a user's preferences
# and then add up the total for their order and tell them 
#how much they need to pay
# Instruction
# Small pizza(S):$15
# Medium pizza(M):$20
# Large Pizza(L):$25
# Add peperoni for small pizza (Y or N): +$2
# Add peperoni for medium or large pizza(Y or N): +$3
# Add extra cheese for any size izza (Y or N): +$1
# 
# todo: work out how much they need to pay based on their size choice.
# todo: work out how much to add to their bill based on their pepperoni choice.
# todo: work out their final amount based on whether if they want extra cheese. 

print("Welcome to python Pizza Deliveries\n")

size = input("What size pizza do you want? S, M or L: \n")
bill = 0

if size == "s":
    print("Your bill is $15")
    bill = 15
    pepperoni = input("do you want pepperoni or your pizza? Y or N: \n")
    if pepperoni == "y":
        bill += 2
        print(f"your  new bill is ${bill}")
    
    else:
        bill = 15
        print(f"your new bill is ${bill}")    
        

elif size == "m":
    print("Your bill is $20")
    bill = 20
    pepperoni = input("do you want pepperoni or your pizza? Y or N: \n")
    if pepperoni == "y":
        bill += 3
        print(f"your bill is {bill}")
    
    else:
        bill = 20
        print(f"your bill is {bill}")

elif size == "l":
    print("You bill is $25")
    bill = 25
    pepperoni = input("do you want pepperoni or your pizza? Y or N: \n")
    if pepperoni == "y":
        bill += 3
        print(f"your bill is {bill}")
    
    else:
        bill = 25
        print(f"your bill is {bill}")             
    

extra_cheese = input("Do you want extra cheese? Y or N: \n")
if extra_cheese == "y":
    bill +=1
    print(f"Your final bill is ${bill}")

