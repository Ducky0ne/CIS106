counter = 0
starting_number = 1
next_number_to_add = 1
next_number_in_sequence = 0

print (starting_number)
print (next_number_to_add)

while counter < 18:
    next_number_in_sequence = starting_number + next_number_to_add
    starting_number = next_number_to_add
    next_number_to_add = next_number_in_sequence

    counter = counter + 1

    print (next_number_in_sequence)