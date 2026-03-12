# INPUTS AND TYPE CASTING
# inputs and type casting are very closely linked
# both allow for gathering inputs from the user and changing the type

# INPUTS
# inputs can be gathered from the console using the input function

# the input function returns a string which is the data that the user entered
# you can store this in a variable as shown below
# input waits until the user presses enter before continuing
user_input = input('Message to show the user before entering some data: ')

# TYPE CASTING
# type casting is the process of changing the type of a variable or piece of data
# this is important for changing the type of inputs and other data to be compatible with the current functionality
# for example, you can not use less than on a string. so, you must first convert the string to an integer

# you can change the type of data by using the name of the type as a function
# placing the original data in the brackets converts the type
integer_number = 23
float_number = float(integer_number)

# not a number
string_number = '123'
integer_from_string = int(string_number)

# all type names can be found in the first tutorial

# you can convert a user input to an integer, or any other type
# some type conversion may do things that are unexpected to you
user_input = input('Number, please: ')
input_as_int = int(user_input)

# this could also be written as shown below
input_as_int = int(input('Number, again please: '))

# this could cause errors if the user does not enter a number
# we will learn about this later