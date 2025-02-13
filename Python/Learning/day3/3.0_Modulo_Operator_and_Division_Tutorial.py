# Modulo operator

# Understanding the Modulo Operator in Python

# Example 1: Modulo with a clean division (no remainder)
# 10 divided by 5 is exactly 2 with no remainder.
result_division = 10 / 5  # 2 is the outcome of the division
result_modulo = 10 % 5    # 0 is the remainder, as 10 is divisible evenly by 5

print("10 / 5 =", result_division)  # Outputs: 2
print("10 % 5 =", result_modulo)    # Outputs: 0

# Example 2: Modulo with an unclean division (with remainder)
# 10 divided by 3 results in a decimal (3.3333333...) because 3 is not a factor of 10.
result_division = 10 / 3  # This will result in a decimal value
result_modulo = 10 % 3    # 1 is the remainder because 3 goes into 10 three times, with 1 left over

print("10 / 3 =", result_division)  # Outputs: 3.3333333...
print("10 % 3 =", result_modulo)    # Outputs: 1