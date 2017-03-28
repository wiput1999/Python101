seconds = int(input("Second :"))


if seconds >= 31104000: year, seconds = divmod(seconds, 31104000); print('year', year)
if seconds >= 2592000: month, seconds = divmod(seconds, 2592000); print('month', month)
if seconds >= 86400: day, seconds = divmod(seconds, 86400); print('day', day)
if seconds >= 3600: hour, seconds = divmod(seconds, 3600); print('hour', hour)
if seconds >= 60: minute, seconds = divmod(seconds, 60); print('minute', minute)
if seconds >= 1: print('second', seconds)




























#Loop vesion


#units = (
#	('year', 12),
#	('month', 30),
#	('day', 24),
#	('hour', 60),
#	('minute', 60),
#	('second', 1)
#)



#result = {}
#x = 0
#while x < len(units):
#	big = 1
#	
#	y = x
#	while y < len(units):
#		big *= units[y][1]
#		y += 1
#		
#	print(units[x][0], big)
#		
#	if seconds >= big:
#		value, seconds = divmod(seconds, big)
#		result[units[x][0]] = value
#
#	x += 1
#
#print(result)