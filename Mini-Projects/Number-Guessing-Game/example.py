# import random for the randint function
import random


# function to begin a gameloop

# turns is the number of turns you get to guess the number
# min_number is the minimum random number
# max_number is the maximum random number

def gameloop(turns=6, min_number=1, max_number=100):
    # the number of turns remaining is the number of turns that you have
    turns_remaining = turns

    # store the number that needs to be guessed
    # it is a random number between and including min and max number
    number_to_guess = random.randint(min_number, max_number)

    # check for if the user has won
    # by default, the player has not won
    # only say that the user wins if they guess correctly
    has_won = False

    # loop forever
    # loop management is in the loop
    while True:
        # get the user's guess and convert to an integer
        guess = int(input('Guess: '))

        # if the user is correct, set the win flag to true and break out of the loop
        if guess == number_to_guess:
            has_won = True
            break

        # remove one turn from the number of turns remaining
        # prevents skipping a turn
        turns_remaining -= 1

        # if there are no turns remaining, leave the loop
        if turns_remaining <= 0:
            break
        
        # if there are turns remaining, show either higher or lower

        # because we don't want to show this message before the win or lose message on the final turn,
        # we increment the turns before the turns_remaining check and the code below
        
        # if the guess is less that the number_to_guess, the number to guess it greater
        # so, show the higher message
        if guess < number_to_guess:
            print('Higher')

        # because we have not won and the number is not higher, it must be lower
        else:
            print('Lower')
        
    # once we exit the loop, show the message based on if the user has won or not
    if has_won:
        print('You win!')
    else:
        print(f'You lose! The number was {number_to_guess}')


# call the gameloop function to begin a gameloop
# the use of a function makes it more modular (could allow for the use of menu system)
gameloop()