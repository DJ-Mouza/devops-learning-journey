# Python Tutorial: String Length and Type Conversion

# Prompt the user to enter their name
name_of_the_user = input("Enter your name: ")

# Calculate the length of the user's name
length_of_the_name = len(name_of_the_user)

# Check and display the data types of the string and the length of the name
print(type("Number of letters in your name: "))  # Displays the type of the string (should be 'str')
print(type(length_of_the_name))                  # Displays the type of the length (should be 'int')

# Concatenate the string and the integer by converting the integer to a string using str()
print("Number of letters in your name: " + str(length_of_the_name))  # Convert int to str for concatenation