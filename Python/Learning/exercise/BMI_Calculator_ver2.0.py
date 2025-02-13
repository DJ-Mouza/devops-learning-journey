# BMI Calculator with Interpretations

# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"
# weight = var1
#height = var2
#bmi = weight / (height**2)
# Refer to this graphic for help:

weight = float(input("Whatis your weight in Kg?"))
height = float(input("What is your height in m?"))

bmi = weight / (height**2)

new_bmi = round(bmi, 1)

if new_bmi < 18.5:
    print("Underweight")

elif new_bmi <= 25:
    print("normal weight")

else:
    print("Overweight")        