# Example of function with type error

print(len("Hello"))       # return an integer

#print(len(12345))         # return an error ( integer has no len() ), the len function calculate the number of characters from a string " ".

#print(len(1.3456))        # return an error ( float has no len() ), the len function calculate the number of characters from a string " ".


# Indentifying data type:

print(type("abc"))      # return class 'string'

print(type(123))        # return class 'interger'

print(type(2.456))      # return class 'float' 

print(type(True))       # return class 'boolean'


# Type conversion:


int("123")

print(int("123"))              # convert the string "123" to an integer


# int("abc") 

# print(int("abc"))            # return a value Error as the string "abc" cannot be converted to a number

float(3456)

print(float(3456))             # convert the interger to a float


float("1.2345")

print(float("1.2345"))         # convert the string to a float


# float(abc)

# print(float(abc))            #retun NameError 'abc' cannot be converted to float as it cannot be converted to a number 



