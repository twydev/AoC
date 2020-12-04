with open('input.txt', 'r') as f:
    password_db = f.readlines()

def parse(raw_entry):
    policy, password = entry.split(':')
    limits, required_char = policy.split()
    lowerbound, upperbound = [int(limit) for limit in limits.split('-')]
    return password, required_char, lowerbound, upperbound

def is_valid_password_by_count(raw_entry):
    password, required_char, lowerbound, upperbound = parse(raw_entry)
    count = count_char(required_char, password)
    return lowerbound <= count and count <= upperbound

def count_char(char, text):
    count = 0
    for letter in text:
        if char == letter:
            count += 1
    return count

# count = 0
# for entry in password_db:
#     if is_valid_password_by_count(entry):
#         count += 1
# print(count)

def is_valid_password_by_position(raw_entry):
    password, required_char, lowerbound, upperbound = parse(raw_entry)
    return (password[lowerbound] != password[upperbound]) and (required_char in [password[lowerbound], password[upperbound]])


count = 0
for entry in password_db:
    if is_valid_password_by_position(entry):
        count += 1
print(count)