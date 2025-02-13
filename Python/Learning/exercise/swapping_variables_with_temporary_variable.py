# Python Tutorial: Swapping Two Variables

# Initial values for glass1 and glass2
glass1 = "milk"
glass2 = "juice"

# Print initial values of glass1 and glass2
print("Before swapping:")
print(f"glass1 contains: {glass1}")
print(f"glass2 contains: {glass2}")

# Swap the values of glass1 and glass2 using a temporary variable

# Store the value of glass1 in a temporary variable
temp_var = glass1

# Assign the value of glass2 to glass1
glass1 = glass2

# Assign the value of the temporary variable (original glass1) to glass2
glass2 = temp_var

# Print the new values of glass1 and glass2 after swapping
print("\nAfter swapping:")
print(f"glass1 contains: {glass1}")
print(f"glass2 contains: {glass2}")