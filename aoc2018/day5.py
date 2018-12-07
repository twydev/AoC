scriptname_list = __file__.split("/")
filename = scriptname_list[-1].split(".")[0] + ".txt"
scriptname_list[-1] = "inputs/" + filename
full_filename = "/".join(scriptname_list)
handle = open(full_filename, "r")

inp = handle.read().rstrip()
inp_l = list(inp)
# inp_l = list("dabAcCaCBAcCcaDA")

matches = set([chr(x) + chr(y) for x, y in zip(xrange(ord('a'),ord('z')+1), xrange(ord('A'),ord('Z')+1) )])
second = set([chr(x) + chr(y) for x, y in zip(xrange(ord('A'),ord('Z')+1), xrange(ord('a'),ord('z')+1) )])
matches = matches.union(second)

def react(inp_list):
	i=0
	while i+1 < len(inp_list):
		char1 = inp_list[i]
		char2 = inp_list[i+1]
		if (char1 + char2) in matches:
			char2 = inp_list.pop(i+1)
			char1 = inp_list.pop(i)
			i-=1
			if(i<0):
				i = 0
		else:
			i+=1
	return inp_list

inp_l = react(inp_l)
print("Starting Length: ",len(inp_l))

count = []
for small, caps in zip(xrange(ord('a'),ord('z')+1), xrange(ord('A'),ord('Z')+1)):
	filtered_list = filter(lambda element: element != chr(small) and element != chr(caps), inp_l)
	reduced_list = react(filtered_list)
	print("Eliminated '" + chr(small) + "' : length", len(reduced_list))
	count.append(len(reduced_list))

# print(count)
print(min(count))