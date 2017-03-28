import sys

n = int(input("n :"))

a = 1

while a <= 2*n-1:
	b = 1
	while b <= 2*n-1:
		if b == a:
			sys.stdout.write("x")
		elif b == 2*n-a:
			sys.stdout.write("x")
		else:
			sys.stdout.write("-")
		b+=1
	a+=1
	print()