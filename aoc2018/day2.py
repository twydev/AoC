scriptname_list = __file__.split("/")
filename = scriptname_list[-1].split(".")[0] + ".txt"
scriptname_list[-1] = "inputs/" + filename
full_filename = "/".join(scriptname_list)
print(full_filename)
handle = open(full_filename, "r")

### Depending of Challenge, read file accordingly ###

str_list = handle.read().split("\n")

import collections
twos = 0
threes = 0
for box_id in str_list:
    counts_map = collections.Counter(box_id)
    values = counts_map.values()
    if 2 in values:
        twos += 1
    if 3 in values:
        threes += 1
print("Twos",twos)
print("Threes",threes)
print(twos*threes)

# for part two, try to convert string to binary