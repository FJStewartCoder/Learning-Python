# BASIC OPERATORS
# operators are similar in nature to mathematics
# they get results of basic operations
# all operators can be used on variables and data

# ADDITION
# the addition operator + adds two or more values
# addition can be performed on numerical, string, list and more types
addition1 = 10 + 2
addition2 = "hello" + " world"
addition3 = 123.0 + 0.456
addition4 = [1, 2, 3, 4, 5] + [6, 7, 8, 9, 10]

# SUBTRACTION
# the subtraction operator - subtracts two or more values
# subtraction is possible on numerical types
subtraction1 = 10 - 20
subtraction2 = 543.21 - 43.21

# DIVISION
# the division operator / divides two or more values
# division is possible on numeric types
division1 = 20 / 2
division2 = 123 / 45

# MULTIPLICATION
# the multiplication operator * multiplies values
# multiplication is possible on numerical, string, list and more types
multiplication1 = 12 * 34
multiplication2 = 123.45 * 67.89
multiplication3 = "hello " * 3
multiplication4 = [1, 2, 3] * 4 

# ASSIGNMENT
# the assignment operator = assigns a variable to a value
# variables can be set to other variables
# multiple assignments can happen simultaneously by seperating values with commas
assignment1 = 123
assignment2 = assignment1
assignment3, assignment4 = 3, 4

# EQUALITY
# the equality operator == checks if two pieces of data have the same value
equality1 = 123 == 7
equality2 = "hello" == "hello"

# INEQUALITY
# the inequality operator != checks if two pieces of data do not have the same value
equality1 = 123 != 7
equality2 = "hello" != "hello"

# GREATER THAN
# the greater than operator > checks if value one is greater than value two
greater_than1 = 10 > 5
greater_than2 = 123.34 > 456.789

# LESS THAN
# the less than operator < checks if value one is less than value two
less_than1 = 12 < 123
less_than2 = 654.321 < 123.45

# GREATER THAN EQUAL TO
# the greater than or equal to operator >= checks if value one is greater than or equal to value two
greater_than_or_equal1 = 10 >= 10
greater_than_or_equal2 = 123.34 >= 456.789

# LESS THAN EQUAL TO
# the less than or equal to operator <= checks if value one is less than or equal to value two
less_than_or_equal1 = 12 <= 12
less_than_or_equal2 = 654.321 <= 123.45

# LOGICAL
# AND
# the keyword "and" checks if two values are both true
and1 = True and False
and2 = (1 == 1) and (2 < 100)

# OR
# the keyword "or" checks if one of the two values are the true
or1 = True or False
or2 = (1 == 'Bob') or (23 > 10)

# NOT
# the keyword "not" inverts the true or false value and can be combined with other operators
not1 = not False
not2 = not True
not3 = not ('Bob' == 7)

# IDENTITY
# IS
# the keyword "is" checks if two boolean/none values are the same
# "is" and == have the same purpose but "is" is exclusive to booleans
is1 = True is True
is2 = (1 < 12) is True

# IS NOT
# the keyword sequence "is not" inverts the operation of "is"
is_not1 = (1 == 1) is not False 

# OWNERSHIP
# IN
# the keyword "in" checks if a value is in a list
# STRING being a LIST or CHARACTERS is important here
in1 = 'a' in 'Hello, World!'
in2 = 5 in [1, 2, 3, 4]
in3 = 8 in [1, 1, 2, 3, 5, 8, 13, 21]

# NOT IN
# the keyword sequence "not in" checks if a value is not in a list
in1 = 'a' not in 'Hello, World!'
in2 = 5 not in [1, 2, 3, 4]
in3 = 8 not in [1, 1, 2, 3, 5, 8, 13, 21]


# ADVANCED OPERATORS

# MODULUS
# the modulus operator % gets the remainder of a division
# for example 10 % 3 = 1 because 3 goes into 10 3 times and leaves you with 1 remaining
mod1 = 10 % 3
mod2 = 123 % 45

# FLOOR DIVISION
# the floor division operator // divides two values and if it has any decimal points, removes them
# for example 10 // 3 = 3 because it would be 3.333 but remove .333
floor_div1 = 10 // 3
floor_div2 = 11 // 3

# EXPONENTIATION
# the exponentiation operator ** gets the power of value one to the power of value two
expo1 = 10 ** 2
expo2 = 2 ** 6

# SUFFIX ANY OPERATOR WITH =
# you can add the = suffix to any operator to reassign the result to the variable
# this can be done on any operator
# for example, +=, -=, *=, /=, %=
example_variable = 10

# the below two lines do the same thing
example_variable += 10
example_variable = example_variable + 10

# BITWISE
# these operators perform operations to the bits of a numerical value
# please look up these if you need to learn about them

# bitwise and (&)
# bitwise or (|)
# bitwise xor (^)
# bitwise not (~)
# bit shifting (>> and <<)