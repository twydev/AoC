scriptname_list = __file__.split("/")
filename = scriptname_list[-1].split(".")[0] + ".txt"
scriptname_list[-1] = "inputs/" + filename
full_filename = "/".join(scriptname_list)
handle = open(full_filename, "r")

inp = handle.read().split("\n")
# inp = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]

fabric = set()
overlap = set()
for claim in inp:
	info = claim.split()
	coords = tuple(map(int,info[2][:-1].split(",")))
	dim = map(int,info[-1].split("x"))
	for x in xrange(dim[0]):
		current_x = coords[0] + x + 1
		for y in xrange(dim[1]):
			current_coords = (current_x, coords[1] + y +1)
			if current_coords not in fabric:
				fabric.add(current_coords)
			else:
				overlap.add(current_coords)
print(len(overlap))

for claim in inp:
	info = claim.split()
	claim_id = info[0]
	coords = tuple(map(int,info[2][:-1].split(",")))
	dim = map(int,info[-1].split("x"))
	hit = False
	for x in xrange(dim[0]):
		current_x = coords[0] + x + 1
		for y in xrange(dim[1]):
			current_coords = (current_x, coords[1] + y +1)
			if current_coords in overlap:
				hit = True
				break
		if (hit):
			break
	if not hit:
		print(claim_id)
		break