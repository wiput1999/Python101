import sys

a = 10
b = 1

c = 1
d = 1

while a > 0:
	b = 1
	while b < a:
		sys.stdout.write("_")
		b+=1
	while c <= d:
		sys.stdout.write("x")
		c+=1
	
	d+=1
	c =1
	a-=1
	sys.stdout.write("\n")