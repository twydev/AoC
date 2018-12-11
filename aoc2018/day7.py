# for linux
# scriptname_list = __file__.split("/")
# filename = scriptname_list[-1].split(".")[0] + ".txt"
# scriptname_list[-1] = "inputs/" + filename
# full_filename = "/".join(scriptname_list)
# print(full_filename)

# for windows
scriptname_list = __file__.split("\\")
filename = scriptname_list[-1].split(".")[0] + ".txt"
scriptname_list[-1] = "inputs\\" + filename
full_filename = "\\".join(scriptname_list)
print(full_filename)
handle = open(full_filename, "r")

inp = handle.read().rstrip().split("\n")
# inp = ["Step C must be finished before step A can begin.",
# "Step C must be finished before step F can begin.",
# "Step A must be finished before step B can begin.",
# "Step A must be finished before step D can begin.",
# "Step B must be finished before step E can begin.",
# "Step D must be finished before step E can begin.",
# "Step F must be finished before step E can begin."]

parent_child_map = {}
child_parent_map = {}
for step in inp:
    parent = step.split()[1]
    child = step.split()[7]
    if parent in parent_child_map:
        parent_child_map[parent].append(child)
    else:
        parent_child_map[parent] = [child]
    if child in child_parent_map:
        child_parent_map[child].append(parent)
    else:
        child_parent_map[child] = [parent]

pc_keys = set(parent_child_map.keys())
cp_keys = set(child_parent_map.keys())

intersect = pc_keys.intersection(cp_keys)
starting_pts = pc_keys.difference(intersect)
ending_pts = cp_keys.difference(intersect)
#print(starting_pts)
#print(ending_pts)

answer = []
while len(starting_pts) > 0:
    frontier = list(starting_pts)
    frontier.sort()
    print("frontier",frontier)
    print("answer",answer)
    for node in frontier:
        if node in child_parent_map:
            print(" node",node,"is not ready to pop yet!")
        else:
            print(" pop node",node)
            answer.append(node) #node is in answer
            if node in parent_child_map:
                for child in parent_child_map[node]: # for each child node
                    starting_pts.add(child) # add child to frontier
                    parents_list = child_parent_map[child] # get all parents of the child
                    parents_list.remove(node) # remove current answer node from all parents list
                    if len(parents_list) == 0:
                        print("   child",child,"lost all parents!")
                        del child_parent_map[child] # remove the child from child-parent map if parents list is totally empty (means all parents done)
            starting_pts.remove(node) 
            break

print("final answer","".join(answer))
