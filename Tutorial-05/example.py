fruits = ['Apple', 'Orange', 'Banana', 'Apple', 'BOB', 'Banana', 'Apple', 'Orange', 'Orange', 'Banana']

counter = 0

for fruit in fruits:
    if fruit == 'BOB':
        break

    print(fruit)

    if fruit != 'Apple':
        continue

    counter = counter + 1

print(counter)

counter = 0

# infinite loop True is always True
while True:
    print(counter)

    counter += 1

    if counter >= 23:
        break
