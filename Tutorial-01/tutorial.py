# THIS IS A CODE COMMENT
'''
THIS IS A
M
U
L
T
I
L
I
N
E
COMMENT
'''

# VARIABLES
# variables a storage location for some data
# the data can be any of the data types shown below
# you can name a variable whatever you like
# PLEASE give them MEANINGFUL names

# if you name two variables with the same name, the first one will be overwritten
# BONUS: this assumes that the variables are in the same scope (will be learned later)
variable = "this is a variable"
variable = "variable now has this value"

# DATA TYPES
# data types are the different types of data that can be stored
# each has unique properties

# STRING (str)
# a string is a LIST of CHARACTERS ( this becomes important later )
# strings are written by either using "" or '' surrounding the string
# the variable with the name "string_variable" stores the value "Hello, World!"
string_variable1 = "Hello, World!"
string_variable2 = 'Hello, World Again!'

# INTEGER (int)
# an integer is any whole positive or negative number
# a whole number being any number with no decimals
int_variable1 = 123
int_variable2 = -123

# FLOAT (float)
# a float or floating point number (has a decimal point) is any positive or negative number
# float values explicitly store decimal points
float_variable1 = 123.456
float_variable2 = -123.456
float_variable3 = 10  # this will be updated to be 10.0

# BOOLEAN (bool)
# a boolean is either a true or false value
# this is useful when creating conditions
bool_variable1 = True
bool_variable2 = False

# LIST (list)
# a list is a list of values of ANY data type
# lists are written using square brackets and values are seperated with a comma []

# BONUS INFO:
# lists are ordered (when indexing the list the data is always in the same place)
# lists length is not fixed
# values in lists are not fixed
# lists allow duplicate data

# the first value in the list has INDEX 0
list_variable = ["INDEX 0", 123, True, ["Another", "list", "wow"], "this is the end"]

# ADVANCED TYPES
# These are types you may encounter but will likely not use whilst learning the basics

# TUPLE (tuple)
# a tuple is list with a fixed length
# tuples are written with brackets ()
tuple_variable = ("abc", 123, -12.345, ["list", "in", "a", "tuple"])

# SET (set)
# a set or hash-set is a storage method allowing for fast data access
# a set is written using curly brackets {}
# all values must be unique
# only some data types can be stored in the set (must be hashable)
# no fixed length
set_variable = {"bob", "triangle"}

# DICTIONARY (dict)
# a dictionary is a set but each KEY has an associated VALUE
# KEYS and VALUES are seperated by a colon :
dict_variable = {
    "bob": "triangle",
    "triangle": "has 3 sides"
}

# NONE (None)
# it stores nothing
none_variable = None