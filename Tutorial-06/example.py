array_2d = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_list)

my_list[5] = 2

print(my_list)

# BONUS TASK

# get each list of the main list
for some_list in array_2d:

    # get each item of the inner list
    for item in some_list:
        print(item)