import sys

n = int(input("n : "))

i = 0
while i <= n:
	for j in range(n-i):
		sys.stdout.write("*")
	print()
	i+=1
		