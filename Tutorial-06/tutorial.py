# LISTS
# a list is method of storing multiple pieces of data, in order, in a single variable 
# lists have several variants. the array-like ones are tuple and list

# LIST
# the list data type is an ordered (always in the same order) list
# you can add and remove items (covered later) from a list
# a list is written with square brackets [] and can contain any data type
example_list = [1, 2, True, None, False, 'Triangle', ['another', 'list']]

# TUPLE
# a tuple is list with a fixed length
# items can not be changed after the tuple is created
# it is written with brackets
example_tuple = ('1', 2, False, 'Bob')

# DATA ACCESS
# you can access data within an array by using the INDEX of the item
# the index is an integer between 0 and the length - 1

# the below array shows the index of the different positions in this array
indexed_list = [0, 1, 2, 3, 4, 5, 6]

# you can use square brackets after a list to get the piece of data at that index
some_number = indexed_list[4]

# this can be performed on a tuple as well
indexed_tuple = (0, 1, 2, 3, 4)

# get the value at index 2 (third position)
another_number = indexed_tuple[2]

# you can set a value in a list, at a specific index as shown below
# index 2 (third item) is now 'Bob'
# you can not do this on the tuple
indexed_list[2] = 'Bob'

# MULTI-DIMENSIONAL ARRAYS

# SLICING