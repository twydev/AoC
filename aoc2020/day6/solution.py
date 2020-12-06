with open('input.txt', 'r') as f:
    form_inputs = f.read().splitlines()

def split_groups_by_blank_lines(entry_list):
    groups = []
    current_group = []
    for entry in entry_list:
        if len(entry) > 0:
            current_group.append(entry)
        else:
            groups.append(current_group)
            current_group = []
    if len(current_group) > 0:
        groups.append(current_group)
    return groups

def convert_group_to_set(group):
    answer_set = set()
    for entry in group:
        for char in entry:
            answer_set.add(char)
    return answer_set

def sum_of_answers(inputs):
    groups = split_groups_by_blank_lines(inputs)
    running_sum = 0
    for group in groups:
        answer_set = convert_group_to_set(group)
        running_sum += len(answer_set)
    return running_sum

def convert_group_to_dict(group):
    answer_dict = {}
    for entry in group:
        for char in entry:
            current_count = answer_dict.get(char, 0)
            answer_dict[char] = current_count+1
    return answer_dict

def sum_of_unanimous_answers(inputs):
    groups = split_groups_by_blank_lines(inputs)
    running_sum = 0
    for group in groups:
        answer_dict = convert_group_to_dict(group)
        running_sum += sum([ 1 for value in answer_dict.values() if value == len(group)])
    return running_sum

print('Sum of answers from all group:', sum_of_answers(form_inputs))
print('Sum of unanimous answers from all group:', sum_of_unanimous_answers(form_inputs))


