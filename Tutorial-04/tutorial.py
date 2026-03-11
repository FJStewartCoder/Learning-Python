# CONDITIONALS
# a condition is a true or false statement that determines the next action
# these can be created in Python with an if statement

number1 = 10
number2 = 5

# IF STATEMENT
# the if statement will run the piece of code that is indented within it if the condition is true
if number1 > number2:
    print('Number 1 is bigger than number 2')

# ELSE
# the if statement can be extended with else to run a different piece of code if the condition is false
if number1 == 70:
    print('Number 1 is 70')
else:
    print('Number 1 is not 70')

# ELIF
# the elif statement (else if) can be used before else to check if another condition is true if all conditions before are false
if number1 == 70:
    print('Number 1 is 70')
elif number1 == 20:
    print('Number 1 is 20')
else:
    print('Number 1 is not 70')

# NESTED IF
# the if statement can be used within another if to check if another condition is true
# only do this if code is before the second if because you could just use "and"
if number2 > 3:
    number2 = 21

    if number2 > 20:
        print('Wow, number2 is bigger than 20')
else:
    print('Number 2 is less than or equal to 3')