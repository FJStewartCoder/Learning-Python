username = 'Bob'
password = 'Triangle'

loops = 3

while loops > 0:
    username_input = input('Username: ')
    password_input = input('Password: ')

    if (username_input == username) and (password_input == password):
        print('Hello', username)
    else:
        print('Please try again!')
    
    loops = loops - 1


users = [
    ('Bob', 'Triangle'),
    ('Jason', 'Archive'),
    ('Timmy', 'Pineapple')
]

loops = 3

while loops > 0:
    # check if the credentials are valid
    valid_credentials = False

    # get the user inputs
    username_input = input('Username: ')
    password_input = input('Password: ')

    # check if the credentials are for any of the accounts
    for account in users:
        current_username = account[0]
        current_password = account[1]

        # if they are, leave this inner loop and set valid to true
        if (username_input == current_username) and (password_input == current_password):
            valid_credentials = True
            break

    # if the credentials are valid, show the welcome message
    if valid_credentials:
        print('Welcome', username_input)
        break
    else:
        print('Try Again')

    # reduce the number of loops remaining by 1 
    loops -= 1