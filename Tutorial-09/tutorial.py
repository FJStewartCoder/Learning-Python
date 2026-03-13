# STRING FORMATTING AND MANIPULATION
# string formatting and manipulation is important when handling inputs and outputs
# most of the time, the user will not enter data in the format you want
# this requires manipulating the string to format it as you want

# often, you will want to write complex strings based on many variables and commas and string addition is frustrating
# use string formatting to improve your strings

# SPECIAL CHARACTERS
# ANSI and escape codes




# ADD CONTENT





# FORMATTING
# string formatting is the process of formatting a string with variables
# there are special methods of writing complex strings without commas or addition

name = 'Bob'
age = 23
favourite_food = 'Ice Cream'

# LEGACY METHOD
# the legacy method or c-style method uses the .format() function to format a string

# create a format by making a string and anywhere a substitution needs to happen use {}

# this is the initial message with no formatting
message = '{} is {} years old and likes to eat {}'

# you can also index the items if you want to do things in a different order
message = '{0} is {1} years old and likes to eat {2}'

# this will substitute the variables in the function (.format)
# in either the order of brackets of the indexes selected
final_message = message.format(name, age, favourite_food)

# it can also be written as below
# this just doesn't use the variable
final_message = '{} is {} years old and likes to eat {}'.format(name, age, favourite_food)

# FORMAT STRINGS
# format strings a special type of string that allows for easier substitution
# prefix any string with the letter "f" to convert it to a formatted string
# use curly brackets to define where a variable will go

# the below example shows how you can substitiute variables into a format string
# this is much nicer to read
final_message = f'{name} is {age} years old and likes to eat {favourite_food}'

# MANIPULATION
# string manipulation involves modifying strings to create alternate strings

# SLICING
# like lists, you can slice strings
# all of the same principles apply so will not be explained here
message = 'Hello, World!'

# only "Hello"
sliced_message = message[:5]

# MANIPULATION FUNCTIONS
# for a full list, I recommend looking a the following list
# https://www.w3schools.com/python/python_strings_methods.asp

# for the more important (and the ones you are most likely to use) see below:


# ADD CONTENT


# .strip
# .split
# .join
#  many more ...