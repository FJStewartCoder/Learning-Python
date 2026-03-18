try:
    int('hello')
except ValueError:
    print('"hello" is not an int')

example_list = [0, 1, 2, 3]

try:
    item = example_list[4]
except IndexError:
    print('You can not access this index because it does not exist')