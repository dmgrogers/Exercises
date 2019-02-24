def getDayOfWeek(num):
	days={1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
	# print(days)
	return days.get(num)  #   # using days[num] would work but throw an error for nonexistent keys


getDayOfWeek(1)
getDayOfWeek(9)  # no output, but no key error if .get() used


# Alternatively, build in some error handling
def getDayOfWeek2(num):
	days={1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
	# print(days)
	try:
		return days[num]  #   # using days[num] would work but throw an error for nonexistent keys
	except KeyError as k:
		return 'Only seven days in the week'

getDayOfWeek2(1)
getDayOfWeek2(9)  # error handled

########################


