# BMI Calculator with Interpretations

# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"
# weight = var1
#height = var2
#bmi = weight / (height**2)
# Refer to this graphic for help:


# Prompt the user to input their weight in kilograms
weight = float(input("What is your weight in Kg?"))

# Prompt the user to input their height in meters
height = float(input("What is your height in m?"))

# Calculate the BMI using the formula: weight / (height squared)
bmi = weight / (height ** 2)

# Round the BMI to one decimal place for easier reading
new_bmi = round(bmi, 1)

# Print out the BMI value for reference
print(f"Your BMI is: {new_bmi}")

# Interpret the BMI based on the following ranges:
# If BMI is under 18.5, print "Underweight"
if new_bmi < 18.5:
    print("Underweight")

# If BMI is between 18.5 (inclusive) and 25 (exclusive), print "Normal weight"
elif new_bmi < 25:
    print("Normal weight")

# If BMI is 25 or over, print "Overweight"
else:
    print("Overweight")
