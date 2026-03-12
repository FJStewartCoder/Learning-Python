people = [
    {
        'name': 'Bob',
        'age': 20,
        'favourite_food': 'Pizza'
    },

    {
        'name': 'Timmy',
        'age': 22,
        'favourite_food': 'Pasta'
    },

    {
        'name': 'Jason',
        'age': 40,
        'favourite_food': 'No Idea'
    },
]

for person in people:
    print(person['name'], person['age'])


names_set = {'Bob', 'Timmy', 'Jason', 'Leon'}
other_names = ['Ashley', 'Timothy', 'Bob']

# go through each name
for name in other_names:

    # if the name is in the names_set, output that the name exists
    if name in names_set:
        print('names_set has name', name)