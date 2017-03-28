import sys

c = 0
for i in range(1,101):
	if i % 2 == 1:
		sys.stdout.write("%s " % i)
		c+=1
	if c == 20:
		c = 0
		print()