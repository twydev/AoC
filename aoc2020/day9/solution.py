with open('input.txt', 'r') as f:
    xmas_messages = [int(message) for message in f.read().splitlines()]

preamble_size = 5

def verify_consistency(preamble_size, message_index, xmas_messages):
    preamble_slice = xmas_messages[message_index - preamble_size:message_index]
    return has_pairwise_matching_sum(preamble_slice, xmas_messages[message_index])

def has_pairwise_matching_sum(values, matching_sum):
    for first_index in range(len(values)):
        for second_index in range(len(values)):
            if first_index == second_index:
                continue
            if values[first_index] + values[second_index] == matching_sum:
                # print('index1', first_index, '->', values[first_index], 'index2', second_index, '->', values[second_index], 'matching', matching_sum)
                return True
    return False

# Part 1
# for index in range(preamble_size, len(xmas_messages)):
#     if not verify_consistency(preamble_size, index, xmas_messages):
#         print(xmas_messages[index], 'is inconsistent. Index:', index)
#         break

error_sum = 15353384
error_index = 502

ending_index = error_index - 1
starting_index = error_index - 2

# Part 2
while starting_index > -1:
    if starting_index == ending_index:
        starting_index -= 1
        continue

    contiguous_slice = xmas_messages[starting_index:ending_index+1]
    contiguous_sum = sum(contiguous_slice)
    # print('evaluating', starting_index, ending_index, contiguous_slice, contiguous_sum)

    if contiguous_sum == error_sum:
        print('starting index', starting_index, 'ending index', ending_index, contiguous_slice)
        print('weakness', min(contiguous_slice) + max(contiguous_slice))
        break

    if contiguous_sum > error_sum:
        ending_index -= 1
        continue
    
    if contiguous_sum < error_sum:
        starting_index -= 1
        continue