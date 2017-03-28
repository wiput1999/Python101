import sys

n = int(input("n :"))

a = n
b = 1

c = 1
d = 2*n-1

while a > 0:
	b = -(a-n)
	while b > 0:
		sys.stdout.write("-")
		b-=1
	while c <= d:
		sys.stdout.write("x")
		c+=1
	
	d-=2
	c =1
	a-=1
	print()