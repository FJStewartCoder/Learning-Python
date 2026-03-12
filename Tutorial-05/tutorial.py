# LOOPS
# loops can be used in programming to do an action multiple times
# this prevents code being copied several times over
# like the if statement, everything that is indented is in the loop

# FOR LOOP
# the for loop loops over an iterable object (an object that you can incrementally go through)
# an example of an iterable is a list. it has a finite length (not always necessary) and you can go through each item in an order 

example_list = ['Item 1', 'Item 2', 'Item 3']

# a for loop is written as shown below
for some_variable in example_list:
    print(some_variable)

# the above example with go through each item in the list and assign the value to the variable that you create
# this is some_variable here

# WHILE LOOP
# the while loop is used to loop until a condition is met
# this is used when you may loop indefinitely

some_condition = True
number = 1

# while loop is written as below
while some_condition is True:
    number = number + 1  # or number += 1

    # when we get here, the loop will be caused to end
    # it will end once we reach the end of the loop
    if number > 10:
        some_condition = False
        print('The loop will end soon')

    # see the message for description 
    # this will run each loop and after the message "The loop will end soon" is shown
    print('This message will still be shown before the loop ends')

print('This is outside of the loop and will run after the loop ends')

# CONTINUE
# the keyword "continue" can be used within a loop to return to the start of the loop
# continue works in both while and for loops

for item in example_list:
    print('This is a message')
    print('The current item is', item)

    # everything after the continue keyword will not be run
    # the is because the loop has begun the next iteration
    continue

    print('You will never see this message')

# BREAK
# the keyword "break" can be used to end a loop before the condition is met or all items have been iterated
# break works in both while and for loops

number = 1

while number < 10:
    print('The current number is', number)

    if number == 3:
        print('The loop will now end')

        # break will end the loop
        # no code after this, in the loop, will be run
        break
    
    print('Adding one to the number')
    number = number + 1

print('The loop ended')