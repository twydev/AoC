with open('input.txt', 'r') as f:
    expenses = f.read()

addends = [int(entry) for entry in expenses.split()]

def find_matching_addends(starting_index, target_value):
    if (starting_index == len(addends) + 1):
        return None
    for index in range(starting_index+1, len(addends)):
        if addends[starting_index] + addends[index] == target_value:
            return addends[starting_index] * addends[index]
    return find_matching_addends(starting_index + 1, target_value)

# print(find_matching_addends(0, 2020))

def find_3_matching_addends(starting_index, target_value):
    if (starting_index == len(addends) + 2):
        return None
    for index in range(starting_index+1, len(addends)):
        candidate = find_matching_addends(index, target_value - addends[starting_index])
        if candidate:
            return candidate * addends[starting_index]
    return find _3_matching_addends(starting_index + 1, target_value)

print(find_3_matching_addends(0, 2020))