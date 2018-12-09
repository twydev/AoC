scriptname_list = __file__.split("/")
filename = scriptname_list[-1].split(".")[0] + ".txt"
scriptname_list[-1] = "inputs/" + filename
full_filename = "/".join(scriptname_list)
handle = open(full_filename, "r")

inp = handle.read().rstrip().split("\n")
inp_l = [tuple(map(int,coords.split(", "))) for coords in list(inp)]
# inp_l = [ (1,1),(1,6),(8,3),(3,4),(5,5),(8,9) ]

area_map = {key : 1 for key in inp_l}
seen = dict()

# print(inp_l)
# print(len(inp_l))
# print(area_map)

xcoord = [coord[0] for coord in inp_l]
ycoord = [coord[1] for coord in inp_l]
x_max = max(xcoord)
x_min = min(xcoord)
y_max = max(ycoord)
y_min = min(ycoord)

# print("x-range: ",x_min,x_max)
# print("y-range: ",y_min,y_max)


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
print("max region",max(area_map.values()))

safe = 10000

def neighbours(coord,step):
	return [(coord[0]-step,coord[1]),
			(coord[0]+step,coord[1]),
			(coord[0],coord[1]-step),
			(coord[0],coord[1]+step)]

def total_dist(coord):
	if coord not in seen:
		total_dist = 0
		for site in inp_l:
			total_dist += dist(coord,site)
		seen[coord] = total_dist
		return total_dist
	else:
		return seen[coord]

def descent(origin_coord, origin_dist, step):
	# print(origin_coord,origin_dist)
	if (origin_dist < safe):
		return origin_coord

	current_dist = origin_dist
	current_coord = origin_coord
	
	while not current_dist < origin_dist:
		for neighbour in neighbours(origin_coord,step):
			new_dist = total_dist(neighbour)
			if new_dist < current_dist:
				current_dist = new_dist
				current_coord = neighbour
		
		if (current_coord != origin_coord):
			return descent(current_coord,current_dist,step)
		else:
			step = step/2

origin = descent((x_min,y_min),total_dist((0,0)),90)
print("origin",origin)

region = set()
region.add(origin)
frontier = set()
frontier.add(origin)

while len(frontier) != 0:
	each = frontier.pop()
	for neighbour in neighbours(each,1):
		# print("Current probe",neighbour)
		if neighbour not in region:
			neighbour_dist = total_dist(neighbour)
			if (neighbour_dist < safe):
				region.add(neighbour)
				frontier.add(neighbour)
	# print("Frontier",frontier)

print("Region Size",len(region))