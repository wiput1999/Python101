import sys

n = 110

for i in range(1,n+1):
	x = 0
	if i % 3 == 0:
		sys.stdout.write("Coza")
		x = 1
	if i % 5 == 0:
		sys.stdout.write("Loza")
		x = 1
	if i % 7 == 0:
		sys.stdout.write("Woza")
		x = 1
	if x == 0:
		sys.stdout.write("%s" % i)
	sys.stdout.write(" ")
	if i % 11 == 0:
		print()