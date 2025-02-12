# Make this like of code run without errors

# print("Numberof letters in your name: " + len(input("Enter your name")))


name_of_the_user = input("Enter your name")

length_of_the_name = len(name_of_the_user)


#check the data type:

print(type("Number of letters in your name: "))      # return class'string'

print(type(length_of_the_name))                      # return class 'int'


# cannot concatenate a class int , we need to do a type conversion from int to string

print("Number of letters in your name: " + str(length_of_the_name))