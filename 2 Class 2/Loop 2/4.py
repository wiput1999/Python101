import sys

a = 1
b = 10

while a <= 10:
	while b >= a:
		sys.stdout.write("x")
		b-=1
	print()
	a+=1
	b = 10