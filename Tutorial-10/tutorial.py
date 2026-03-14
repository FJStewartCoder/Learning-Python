# FUNCTIONS AND SCOPE
# functions and scope both are very well linked
# functions are small pieces of code
# score is a concept relating to where variables exist in you program

# FUNCTIONS
# a function is a piece of code that does something
# functions can be given data and they can return data

# MAKING A FUNCTION
# to make a function you can use the 'def' keyword
# 'def' means define
# use brackets to after the name of the function
# everything indented is in the function

def my_function():
    print('Hello')

def greeting():
    print('Hello, World!')

# CALLING A FUNCTION
# calling or running a function is the process of begining the code in the function
# the code in a function will not run until it is called
# a function must be defined before you use it (definition on line 20 but calling on line 10 is not possible) 

# to call a function, use its name then brackets after it
# (like print or input)
greeting()
my_function()

# RETURN VALUES
# a return value is a value that you get from running a function
# (like input returns the string the user entered)

def return_some_value():
    a = 10
    b = 20

    # use the 'return' keyword to return the value
    # you return any data type
    return a + b

# returned_value becomes the value that is returned from the function
# in this example, returned value will be 30
returned_value = return_some_value()

# greeting returns nothing so returned_value will ne None
returned_value = greeting()

# ARGUMENTS
# arguments are values that you can pass into the function to modify its use

# by writing variable names in the brackets, you create arguments
# these variables can be used in the function
def func_with_arguments(a, b):
    return a + b

# the below example, 10 and 5 are the values that the variables a and b hold
# so a = 10, b = 5
# the function adds a and b and returns the result which is 15
# so value here will be 15
value = func_with_arguments(10, 5)

# arguments also don't have fixed types so you could do this
# value here would be 'hello, world!'
value = func_with_arguments('hello,', ' world!')

# DEFAULT VALUES
# defaults values can be set for your functions if it has multiple functionalities but you want to set defaults

# use = after a variable to set the default value
# if an argument has a default value, no non-default values can be written after
# YOU CAN NOT DO: (a, b, c=5, d) because you could write nothing for c (because it has a default) but you require d
def do_maths(num1, num2, mode='+'):
    if mode == '+':
        return num1 + num2
    if mode == '-':
        return num1 - num2
    if mode == '/':
        return num1 / num2
    if mode == '*':
        return num1 * num2
    else:
        return 0

# by default is + mode
value = do_maths(50, 100)

# can optionally set the mode
value = do_maths(100, 50, '-')

# ADVANCED FUNCTION ARGUMENTS
# these are more advanced functionalities that could be useful when developing complex programs

# POSITIONAL AND KEYWORD ARGS
# positional and keyword are words used to describe the type of an argument

# POSITIONAL
# a positional argument is an argument reliate on the order in which you write it

# here a and b are positional because a comes first and b comes second and you must write the arguments in that order
def func(a, b):
    return a + b

# a=10 and b=50 and the order will always be this. a will never be 50 and b will never be 10
func(10, 50)

# KEYWORD
# keyword arguments are arguments in which you choose to assign a value to a specific variable

# here the code selects the value that will be assigned to each required argument
# these are required because there is no default value
func(b=10, a=50)

# FORCE POSITIONAL
# you may want to write a function where you can not use keyword arguments

# use the / as an argument to set all arguments before it to be force positional
# it will cause an error trying to pass these as keyword arguments
def new_func(a, /, b):
    return a * b

# this will cause an error
new_func(b=10, a=15)

# this is valid
new_func(10, b=15)

# FORCE KEYWORD
# the inverse of force positional is force keyword
# these arguments can only be used if assigned with a keyword

# use the * to force all arguments after to be forced as keyword arguments
def new_new_func(a, *, b):
    return a - b

# this will cause an error
new_new_func(10, 15)

# this is valid
new_new_func(10, b=15)

# ARGS AND KWARGS
# args and kwargs (argument list and keyword arguments list) are methods of accepting any number of arguments
# you can make args and keyword lists using the * and ** symbols respectively

# ARGS
# use * before a variable name to make is an argument list
# if you put an argument after an args list, it becomes keyword only
# you can put arguements before an args list and they will work as expected
def add_many(*numbers):
    result = 0

    # numbers here is a list because it is a list or arguments
    for number in numbers:
        result += number
    
    return result

# this will add all of the numbers together
add_many(10, 15, 70, -10, 34)

# KWARGS
# kwargs or keyword args is a dictionary of keyword arguments

# keyword args are writen using ** before a variable name
# the same rules apply as args
def keyword_func(**kwargs):
    if 'a' in kwargs:
        print(kwargs['a'])


# you can pass as many keywords as you like
keyword_func(a=10, b=15, c=123, d=785)


# RECURSION
# recursion is the concept of running a function from within itself

# this function calls itself from within itself (this example ends up in an infinite loop)
def recusive_func():
    recusive_func()

# READ MORE BELOW:
# https://www.w3schools.com/python/python_recursion.asp


# SCOPE
# scope is a concept relating to where variables and data exist within a program
# there are two scopes: local and global

# GLOBAL
# global scope is a place where everything exists

# this is a global variable
# everywhere in the program can see this variable
some_variable = 'Bob'

# this function can access some_variable because it is in a higher scope
def some_function():
    local_variable = 'Triangle'

    # we can access the variable that exists outside of the function
    print(some_variable)

# the local variable exists only in the function's scope
# we can not access variables that exist in functions
# this will cause an error
print(local_variable)

# it is generally discouraged to define variables at a global scope because everything can access them
# please do not feel like you can not use global variables. they are great for use as settings or constants
# however, there are disadvantages such as being easy to overwrite