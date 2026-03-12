# SETS
# a set or hash-set is a method of storing unordered, unique data items
# items in a set are unordered (they may not always be in the same order)
# items in a set are unique (you can not have duplicate data in a set)

# BONUS
# sets function by assigning each item a number (a hash, which is number)
# the item is stored at the index of the hash (there is a bit more but this is basically what it does)
# instead of looking through each item to find something, you can just look at the index corrolating to the hash
# this is very fast but clearly you can not have duplicate items

# sets are written using curly brackets {} (like a dictionary)
example_set = {'Bob', 'Timmy', 'Tina', 'Oscar'}

# this is much faster when using a set because you don't need to check each item
if 'Bob' in example_set:
    print('example_set has Bob')

# DICTIONARIES
# a dictionary is an extension of a set where each KEY has an assigned VALUE
# you can make a dictionary using curly brackets {}
# KEYS and VALUES are seperated by a colon :

# like a set, KEYS must be unique
# a dictionary is equally fast to access data as a set

# our example here is a simple profile of Bob
# like a list, a dictionary can be written over several lines
example_dictionary = {
    'name': 'Bob',
    'age': 12,
    'likes': ['Football', 'Triangles', 'Cake']
}

# or on one (for some reason)
# this is really hard to read
example_dictionary = {'name': 'Bob', 'age': 12, 'likes': ['Football', 'Triangles', 'Cake']}

# to access data in a dictionary, you can use square brackets []
name = example_dictionary['name']

# or you can use the get function
# this is a safer for data access because you can set default values
name = example_dictionary.get('name')

# to set new data in a dictionary, invert the operation (like a list)
# if the data does not exist, it will make a new field in the dictionary
example_dictionary['name'] = 'Timmy'