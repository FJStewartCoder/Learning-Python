name = input('Name: ')

# convert the age to a number for processing
age = int(input('Age: '))

if age > 50:
    print(f'{name}\nYou are {age} years young.')
else:
    print(f'{name}\nYou are {age} years old.')

# BONUS TASK

# split at the space character (space is default)
name_list = name.split()

for name in name_list:
    # first convert to lowercase so all lower then only capitalise the first letter
    print(name.lower().capitalize())

if age > 50:
    print(f'You are {age} years young.')
else:
    print(f'You are {age} years old.')