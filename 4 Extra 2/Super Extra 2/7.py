import sys

n = 9

sys.stdout.write(" *  |")
for i in range(1,n+1):
	sys.stdout.write("  %s" % i)
print()
print("---------------------------------")

for i in range(1,n+1):
	sys.stdout.write(" %s  |" % i)
	for j in range(1,n+1):
		res = i*j
		if res < 10:
			sys.stdout.write("  %s" % res)
		else:
			sys.stdout.write(" %s" % res)
	print()
		