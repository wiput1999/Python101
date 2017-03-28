import random
import sys

for i in range(4):
	for j in range(25):
		sys.stdout.write("%s " % random.randrange(1,100))
	print()