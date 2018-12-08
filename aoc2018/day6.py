scriptname_list = __file__.split("/")
filename = scriptname_list[-1].split(".")[0] + ".txt"
scriptname_list[-1] = "inputs/" + filename
full_filename = "/".join(scriptname_list)
handle = open(full_filename, "r")

inp = handle.read().rstrip().split("\n")
inp_l = [tuple(map(int,coords.split(", "))) for coords in list(inp)]
# inp_l = [ (1,1),(1,6),(8,3),(3,4),(5,5),(8,9) ]

area_map = {key : 1 for key in inp_l}

# print(inp_l)
print(len(inp_l))
# print(area_map)

xcoord = [coord[0] for coord in inp_l]
ycoord = [coord[1] for coord in inp_l]
x_max = max(xcoord)
x_min = min(xcoord)
y_max = max(ycoord)
y_min = min(ycoord)

print("x-range: ",x_min,x_max)
print("y-range: ",y_min,y_max)


def dist(coord_a, coord_b):
	return abs(coord_a[0] - coord_b[0]) + abs(coord_a[1] - coord_b[1])

border = set()
upperbound = dist((x_min,y_min),(x_max,y_max))
for x in xrange(x_min,x_max+1):
	for y in xrange(y_min,y_max+1):
		current_coord = (x,y)
		if current_coord not in area_map:
			nearest_dist = upperbound
			nearest_site = ()
			for site in inp_l:
				mh_dist = dist(current_coord, site)
				if (mh_dist < nearest_dist):
					# found new nearest site
					nearest_dist = mh_dist
					nearest_site = site
				elif (mh_dist == nearest_dist):
					# there is a tie
					nearest_site = ()
			if nearest_site != ():
				area_map[nearest_site] = area_map[nearest_site] + 1
				# check border cases
				if (x in (x_min,x_max)) or (y in (y_min,y_max)):
					# this site is a border
					border.add(nearest_site)

for key in border:
	del area_map[key]
print(max(area_map.values()))

# part 2 can consider using some kind of gradient descent methond
# to find the region, then start from there