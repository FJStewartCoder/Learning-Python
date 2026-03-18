# ERROR HANDLING
# error handling is the process of taking action against an error
# instead of crashing when an error happens, you can continue the program

# TRY
# the try keyword allows you to try an action in a safe environment where you can handle errors

# to try to do an action, place it within a try
try:
    # action to try
    int('Hello')

# select the error name for the error you want to handle
except ValueError:
    # action to take if an error happens
    print('Hello is not a valid integer')

# FIXING ERRORS
# fixing and identifying errors

# you many get an error as seen below
'''
Traceback (most recent call last):
  File "Learning-Python/Tutorial-13/tutorial.py", line 15, in <module>
    int('ehhlo')
    ~~~^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'ehhlo'
'''

# to use this error message, see what it tells you
# it tells you the filename and line "tutorial.py" and line 15

# check this line in this file
# or look for the code that it underlines
# int('ehhlo')

# then, you get the error name
# ValueError: ...

# so, the error name is ValueError (you can use this in expect)
# this error tells you a little bit about what happened

# this error is telling us
# invalid literal for int() with base 10: 'ehhlo'

# this means that 'ehhlo' is not a number (which is obvious)
# this allows us to find the error name to use within a try
# and helps us to fix the error

# RAISING ERRORS
# use the raise keyword to raise an error

# creates a ValueError
raise ValueError