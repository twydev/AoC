with open('input.txt', 'r') as f:
    rules = f.read().splitlines()

import re
def parse_rule(rule):
    child_bag_pattern = r'\d+ \w+ \w+'
    compiled_matcher = re.compile(child_bag_pattern)
    child_bags = compiled_matcher.findall(rule)
    child_map = {}
    for child_bag in child_bags:
        tokens = child_bag.split()
        child_map[tokens[1] + ' ' + tokens[2]] = int(tokens[0])
    parent_bag_pattern = r'^\w+ \w+'
    parent_bag = re.match(parent_bag_pattern, rule).group(0)
    return parent_bag, child_map

def create_hierarchy_maps(rules):
    parent_to_child_map = {}
    child_to_parent_map = {}
    for rule in rules:
        parent_bag, child_map = parse_rule(rule)
        parent_to_child_map[parent_bag] = child_map

        for child_bag in child_map.keys():
            parents_list = child_to_parent_map.get(child_bag, [])
            parents_list.append(parent_bag)
            child_to_parent_map[child_bag] = parents_list
    return parent_to_child_map, child_to_parent_map

def prettyPrint(dictionary):
    for key, value in dictionary.items():
        print(key, value)

def get_all_ancestors(child, child_map):
    parent_list = child_map.get(child, [])
    current_ancestors = set(parent_list)
    grand_ancestors = set([])
    for each_parent in current_ancestors:
        grand_ancestors = grand_ancestors.union(get_all_ancestors(each_parent, child_map))
    return current_ancestors.union(grand_ancestors)

def count_all_children(parent, parent_map):
    current_children = parent_map[parent]
    # base case
    running_sum = 0
    if len(current_children) > 0:
        for child, quantity in current_children.items():
            running_sum += quantity + quantity * count_all_children(child, parent_map)
    return running_sum

parent_map, child_map = create_hierarchy_maps(rules)
# print('All ancestors of Shiny Gold bag:', len(get_all_ancestors('shiny gold', child_map)))
print('All children of Shiny Gold bag:', count_all_children('shiny gold', parent_map))

