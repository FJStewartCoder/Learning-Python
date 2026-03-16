# FILE HANDLING
# file handing is the process of reading or writing to files
# files are permenant unlike variables and can store anything

# OPENING AND CLOSING FILE
# opening a file means that you express intent to use the file
# you must close the file after use to allow other programs to also use the file

# open a file using the open function
# 'filename.txt' is the name of the file to open
my_file = open('filename.txt')

# close the file using the close function on the file variable
# if you do not close the file, other programs will be unable to use the file

# if you have ever seen the "You can not delete this file because it is in use" error
# this is the cause
my_file.close()

# you can also use an alternate method of accessing a file using the "with" keyword
with open('filename.txt') as my_file:
    # use my_file within this block
    # my_file is the file variable

    # this file is automatically closed at the end of the code block

    pass  # does nothing

# FILE MODES
# file modes are the different modes that you can open a file in
# each has it's own purpose

# READ (r)
# to read to a file, open the file in read mode
# read mode is accessed using 'r'

# read mode will read from a file that exists
# if the file does not exist, an error will occur

# open the file in read mode. the second argument is the file mode
with open('filename.txt', 'r') as f:
    pass

# WRITE (w)
# to write to a file, open the file in write mode
# write mode is accessed using 'w'

# write mode gives you a blank file to write to
# write mode will create a file if it does not exist

# open a file in write mode
with open('filename.txt', 'w') as f:
    pass

# APPEND (a)
# to add more content to a file, open the file in append mode
# append mode is accessed using 'a'

# append mode creates a file if it does not exist
# append mode adds new content to a file and does not overwrite existing content

# open a file in write mode
with open('filename.txt', 'a') as f:
    pass

# CREATE (x)
# to create a new file, open the file in create mode
# create mode is accessed using 'x'

# create mode creates a file if it does not exist
# causes an error if the file exists

# create a new file using create mode
with open('different_filename.txt', 'x') as f:
    pass

# READ/WRITE (+)
# read/write extension mode allows for adding functionality to read or write modes
# this mode is accessed using '+' after a previous mode

# if the file is in read mode, adds write functionality
# if the file is in write or append mode, adds read functionality

# the default mode is the one selected, but gives other functionality
# so 'r+' will not create a new file but 'w+' will

# open the file in read mode with write functionality
with open('filename.txt', 'r+') as f:
    pass

# open the file in write mode with read functionality
with open('filename.txt', 'w+') as f:
    pass

# open the file in append mode with read functionality
with open('filename.txt', 'a+') as f:
    pass

# BINARY (b)
# to use a file in binary mode, open the file with binary mode
# binary mode is accessed using 'b'

# add the 'b' character to any other mode to add binary functionalities
# for example, the number 123 will be written as a single byte character rather than the characters '123'

# open a file in read mode; read as binary and allow for writing
with open('filename.txt', 'rb+') as f:
    pass


# READ
# reading a file is reading data from a file that exists

with open('filename.txt', 'r') as my_file:
    # the read function reads the entire file
    # or
    # some number of specified charcters
    some_data = my_file.read()

    # reads 10 characters (you probably won't use this often)
    some_data = my_file.read(10)

    # the readline function reads until a newline character '\n'
    # that is, it reads a line
    some_data = my_file.readline()

    # the readlines function reads some number of lines
    # this would read 5 newlines
    some_data = my_file.readlines(5)

# WRITE
# writing data to a file

with open('filename.txt', 'w') as my_file:
    # the write function writes some data to the file
    # it does not automatically add a new line
    my_file.write('This will be written to the file')

    # the writelines function writes some number of lines to a file
    # each one is seperated by a new line
    
    # it takes an iterable as an argument
    my_file.writelines([
        'line1',
        'line2',
        'line3'
    ])