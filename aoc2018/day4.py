scriptname_list = __file__.split("/")
filename = scriptname_list[-1].split(".")[0] + ".txt"
scriptname_list[-1] = "inputs/" + filename
full_filename = "/".join(scriptname_list)
handle = open(full_filename, "r")

# inp = ["[1518-11-01 00:00] Guard #10 begins shift",
# "[1518-11-01 00:05] falls asleep",
# "[1518-11-01 00:25] wakes up",
# "[1518-11-01 00:30] falls asleep",
# "[1518-11-01 00:55] wakes up",
# "[1518-11-01 23:58] Guard #99 begins shift",
# "[1518-11-02 00:40] falls asleep",
# "[1518-11-02 00:50] wakes up",
# "[1518-11-03 00:05] Guard #10 begins shift",
# "[1518-11-03 00:24] falls asleep",
# "[1518-11-03 00:29] wakes up",
# "[1518-11-04 00:02] Guard #99 begins shift",
# "[1518-11-04 00:36] falls asleep",
# "[1518-11-04 00:46] wakes up",
# "[1518-11-05 00:03] Guard #99 begins shift",
# "[1518-11-05 00:45] falls asleep",
# "[1518-11-05 00:55] wakes up"]

inp = handle.read().split("\n")

inp.sort()
guards = {}
current_id = 0
for log in inp:
	info = log.split()
	event = info[3]
	# print(event)

	if (len(info) > 4):	
		guard_id = int(event[1:])
		if guard_id not in guards:
			guards[guard_id] = [0] * 60
		schedule = guards[guard_id]
	else:
		current_minute = int(info[1][:-1].split(":")[1])
		if (len(event) < 3):
			for minute in xrange(prev_minute,current_minute):
				schedule[minute]+=1
		prev_minute = current_minute

max_sum = 0
max_guard = ""
schedule = []
for guard_id in guards:
	current_sum = sum(guards[guard_id])
	if current_sum > max_sum:
		max_sum = current_sum
		max_guard = guard_id
		schedule = guards[guard_id]
# print(max_guard,max_sum,schedule)
max_minute = max(schedule)
most_common_minute = schedule.index(max_minute)
print(max_guard * most_common_minute)

max_record = 0
max_guard = ""
schedule = []
for guard_id in guards:
	current_max = max(guards[guard_id])
	if current_max > max_record:
		max_record = current_max
		max_guard = guard_id
		schedule = guards[guard_id]
# print(max_guard,max_record,schedule)
most_common_minute = schedule.index(max_record)
print(max_guard * most_common_minute)