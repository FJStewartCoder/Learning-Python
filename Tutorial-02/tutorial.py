# this is a short message to output to the user
message = 'Hello, World from a variable!'

# the print FUNCTION allows you to output data
# since print is a function, it is used by following it with brackets
# data in the brackets is outputted
print('This is a message')

# you can print out most data types
print(123)
print(False)

# you can even output lists
print(["hello", "world", "from", "this", "list"])

# you can also print out variables
print(message)


# the type function allows you to get the type of a variable or piece of data
int_variable = 1234
float_variable = 1234.45
string_variable = 'This is a string'

# the type function returns to you some data
# the return data can be assigned to a variable
# here the data that is returned is printed out
print(type(int_variable))

float_variable_type = type(float_variable)
print(float_variable_type)

print(type(string_variable))

# you can print multiple pieces of data at once by seperating them with commas
# this automatically places a space between each piece of data
print(string_variable, type(string_variable), 'some more data')