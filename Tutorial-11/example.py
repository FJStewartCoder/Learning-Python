# this is needed everywhere, so it is useful to create a variable for it
# if you need to change the name, it will be changed everywhere
filename = 'facts.txt'

def add_fact():
    # ask the user to enter a fact
    fact = input('Enter a fact: ')

    # open the file in append mode
    with open(filename, 'a') as facts_file:
        facts_file.write(f'{fact}\n')


def read_facts():
    # a long string that will store the file data
    raw_facts = ''

    # open the file in read mode
    with open(filename, 'r') as facts_file:
        # read all of the data into the string
        raw_facts = facts_file.read()

    # split the facts by line
    # this will create a list of facts 
    facts = raw_facts.splitlines()

    # loop over the facts and print each one
    for fact in facts:
        print(f'FACT: {fact}')


def clear_facts():
    with open(filename, 'w') as f:
        print('Cleared facts')


# how to decide when to end
running = True

# while running, loop
while running:
    # get the user's selection
    choice = input('(W)rite fact, (R)ead facts, (C)lear facts or (Q)uit: ') 

    if choice == 'w':
        # add a fact
        add_fact()

    elif choice == 'r':
        # read the facts
        read_facts()

    elif choice == 'c':
        # read the facts
        clear_facts()

    elif choice == 'q':
        # end the loop
        running = False

    else:
        # error message
        print('Please try again!')