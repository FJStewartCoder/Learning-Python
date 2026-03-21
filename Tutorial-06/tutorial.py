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

# indexes can also be negative if you want to start at the end
# these go from -1 (first backwards) to negative the length of the list

# the below array shows the index of the different positions in this array
indexed_list = [0, 1, 2, 3, 4, 5, 6]

# you can use square brackets after a list to get the piece of data at that index
# both below get the same number
some_number = indexed_list[4]
some_number = indexed_list[-3]  # because it is third backwards

# this can be performed on a tuple as well
indexed_tuple = (0, 1, 2, 3, 4)

# get the value at index 2 (third position)
another_number = indexed_tuple[2]

# you can set a value in a list, at a specific index as shown below
# index 2 (third item) is now 'Bob'
# you can not do this on the tuple
indexed_list[2] = 'Bob'

# MULTI-DIMENSIONAL ARRAYS
# the works list and array are used interchangable in this context
# a multi-dimensional array is an array of arrays. typically, the inners arrays all have the same length
# this allows for an imaginary rectangular formation

# a 2D array is an array of arrays
# a 3D array is an array of 2D arrays
# and so on...

# lists, as well as most things with brackets, can be written over several lines (as long as the data is in brackets)
array_2d = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# or put it all on one line (probably a bit harder to read)
array_2d = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# this could be used in a game of naughts and crosses (tic-tac-toe)

# to access a 2d array, reference the row first (using an index)
row1 = array_2d[0]  # [1, 2, 3, 4]

# then, reference the column
# use either of the below
value = row1[2]  # index 2 of [1, 2, 3, 4] which is 3
value = array_2d[0][2]  # index 0 of array_2d which is [1, 2, 3, 4] then index 2 of [1, 2, 3, 4] which is 3

# SLICING
# slicing (also applicable to strings) is a method of getting a portion of a list
# slicing is written similarly to indexing but uses a colon : to define the index range

example_list = [0, 1, 2, 3, 4, 5, 6, 7]

# to get a portion from one index to another you can write the following
# this gets from index 2 to index 5 (not including the value at the final index)
smaller_list = example_list[2:5]

# this shows the slice
print(smaller_list)

# if you want from the start to an index, you can omit the 0
# this gets from index 0 to index 5 (still not including this value)
smaller_list = example_list[:5]

# this shows the slice
print(smaller_list)

# if you want to get from an index to the end, you can omit the final index
# this gets from index 2 to the end
smaller_list = example_list[2:] 

# this shows the slice
print(smaller_list)

# LIST FUNCTIONS
# there are several built-in functions to help modify lists
# there are more functions than this but these are the most common useful ones

# reset the list to be blank
example_list = []

# APPEND
# to add a value to the end of the list, use the append function  

# this adds the number 10 to the end of the list
# this function returns nothing
example_list.append(10)

# COPY
# the copy function makes a copy of the current list
# this function returns a list
copied_list = example_list.copy()

# EXTEND
# extend a list with another list
other_list = [1, 2, 3]

# adds the entirety of other_list to the end of example_list
# this function returns nothing
example_list.extend(other_list)

# INDEX
# get the index of an item

# this gets the index of the value 2 in the example list
# this function returns the index of the value if found
# otherwise, it causes an error
found_index = example_list.index(2)

# INSERTION
# insert a value at a specific index

# this inserts the value of 20 at index 0
# so, the value at index a will be value b
# all other values after are moved across by one index

# the function returns nothing
example_list.insert(0, 20)

# POP
# remove a value based on the index

# will remove the value at index 2 and move all values after across by negative one index 
# this function returns nothing
example_list.pop(2)

# REMOVE
# remove the first instance of a value if it exists

# this will remove the first instance of the value 1 from the list
# an error will occur if the value is not in the list
# the function returns nothing
example_list.remove(1)

# REVERSE 
# reverse the list

# this will reverse the order of the list
# the function returns nothing
example_list.reverse()

# SORTING
# sort a list (order is customisable)
# by default, sorts in ascending order (smallest value first)

# this will sort the current list
# this function returns nothing

# you can pass in, optionally, the reverse keyword which will sort in ascending order
# you can also pass in, optionally, a key keyword which is a function used to determine how the sorting will happen
example_list.sort(key=lambda x: x, reverse=True)

# this function is the same as .sort but returns the sorted list
# the same arguments can be passed to sorted
example_list = sorted(example_list)

# LENGTH
# get the length of a list
# this function works on strings also

# this gets the number of items in example list
# the function returns an integer
length = len(example_list)