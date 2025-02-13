# Python Tutorial: BMI Calculation with Rounding

# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# Bmi is equal to the person's weight divided by the person's height squared.
# Convert this sentence into code on line 6. 


# Define the height in meters and weight in kilograms
height = 1.65  # height in meters
weight = 84     # weight in kilograms

# Calculate the BMI using the formula: BMI = weight / (height^2)
bmi = weight / (height ** 2)

# Print the calculated BMI (without rounding)
print("Calculated BMI:", bmi)

# Round the BMI to the nearest whole number and print it
print("Rounded BMI (to nearest integer):", round(bmi))

# Round the BMI to 2 decimal places and print it
print("Rounded BMI (to 2 decimal points):", round(bmi, 2))