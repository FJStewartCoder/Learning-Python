# STRING FORMATTING AND MANIPULATION
# string formatting and manipulation is important when handling inputs and outputs
# most of the time, the user will not enter data in the format you want
# this requires manipulating the string to format it as you want

# often, you will want to write complex strings based on many variables and commas and string addition is frustrating
# use string formatting to improve your strings

# SPECIAL CHARACTERS
# there are some special characters (generally applied, not just Python) that allow you to show or do special things
# these fall into the categories of ANSI or escape codes

# ANSI CODES
# the below resource is incredible for showing all of the ANSI codes
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

# ESCAPE CODES
# escape codes are characters that allow you to do special effects such as a newline or a tab
# all escape codes begin with a backward slash \
# to use the actual backward slash (for some reason) use two in a row \\

# BACKSLASH
# used for a single backslash (a single one tries to become an escape code and causes errors)
backslash = '\\'

# NEWLINE
# after this character, a newline begins
newline = '\n'

# TAB
# writes the four space tab character
tab = '\t'

# RETURN CARRIAGE
# returns the place of writing to the start of the line
# for example 'Hello\rWorld' would show as 'World' because the writing begins back at the start after the return carriage
# another example 'areallylongwordorsomething \rBob' would become 'Boballylongwordorsomething '
# it begins writing back at the start and overwrites the current string
return_carriage = '\r'


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

example_string = 'hello, world!'

# STRING CASE
# these functions all relate to switching the case of characters
# each function returns a new string (just using the function will not modify the string)

# CAPITALISATION
# you can capitalise the first character of a string as shown below
example_string = example_string.capitalize()

# LOWERCASE
# to convert all characters to lowercase (useful when getting user input) use the below function
example_string = example_string.lower()

# UPPERCASE
# to convert all characters to uppercase (useful when getting user input also) use the below function
example_string = example_string.upper()

# PATTERN FINDING
# these functions allow you to find where certain patterns occur in a string

# FIND / INDEX
# you can find a string or character in a string using either of the below functions
# these functions return the index where the pattern is found

found_index = example_string.find('H')  # returns -1 if not found
found_index = example_string.index('WORLD')  # causes an error if not found

# CONDITIONS
# none of these will be covered here because they are only useful in very specific scenarios
# there are usually better things you can do than use these
# all of these functions begin with is...()

# WHITESPACE REMOVAL
# when getting user input (or some other wierd scenarios) you may encounter whitespace around the string
# whitespace if defined as a sequence of space characters (' ') before or after the piece of data
# for example '    my name is Bob     '

# you can remove whitespace from strings using the below functions
# as before, this returns the new string and does not modify the current string

example_string = '  my name is Bob    '

# lstrip removes whitespace from only the start of the string
new_string = example_string.lstrip()

# rstrip removes whitespace from only the right side of the string
new_string = example_string.rstrip()

# strip removes whitespace from both sides of the string
new_string = example_string.strip()

# .strip is equivalent to the below example
new_string = example_string.rstrip().lstrip()

# DIVISION
# you can divide a string into a list of strings, based on a seperator character, by using the split methods
# this is useful in data parsing and user input
# these functions return a list

example_string = 'BOB,JASON,TINA'

# use the .split function, with a seperator character, to split the character into a list of strings
# here with list will contain ['BOB', 'JASON', 'TINA']
names_list = example_string.split(',')

# \n is a new line
example_string = 'Bob\nTina\nJason'

# you can also split by line
names_list = example_string.splitlines()

# this is equivalent to
names_list = example_string.split('\n')

# OTHER
# these other functions are also useful but don't have a category
# they each return a different value

# REPLACEMENT
# replacement involves replacing some characters with other characters

# you use .replace to replace string a with string b
# this function returns a new string
new_string = example_string.replace('a', 'b')

# JOINING
# you can create a join of an iterator of strings as shown below
# this function returns a single string

# the first string here (',') is the joining string
# each item in the list of names will be seperated by the joining character
# this will return 'BOB,TINA,JOHN,JASON'
new_string = ','.join(['BOB', 'TINA', 'JOHN', 'JASON'])

# COUNTING
# the count function is used to count the number of occurances of a string within another string

example_string = 'Apples and Bananas'

# use the .count function to get the number of occurances of a string in another string
# this will count the number of 'a's in the example string
number_of_a = example_string.count('a')