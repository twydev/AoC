
scriptname_list = __file__.split("/")
filename = scriptname_list[-1].split(".")[0] + ".txt"
scriptname_list[-1] = "inputs/" + filename
full_filename = "/".join(scriptname_list)
print(full_filename)
handle = open(full_filename, "r")

### Depending of Challenge, read file accordingly ###

str_list = handle.readlines()
int_list = map(int, str_list)
print(sum(int_list))

seen = set()
frequency = 0
seen.add(frequency)
iteration = 1
while (iteration > 0):
    #print("iteration:", iteration)
    for i in int_list:
        frequency += i
        if frequency in seen:
            print(frequency)
            iteration = -1
            break
        seen.add(frequency)
    iteration += 1