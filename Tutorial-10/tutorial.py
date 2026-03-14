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
#   ARGS AND KWARGS
#   POSITIONAL AND KEYWORD ARGS
# DEFAULT VALUES
# RECURSION

# SCOPE
# GLOBAL
# LOCAL