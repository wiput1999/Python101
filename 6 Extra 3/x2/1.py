import sys

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

if a >= b and a >= c:
	x = a
	y = b
	z = c
elif b >= a and b >= c:
	x = b
	y = a
	z = c
else:
	x = c
	y = b
	z = a

if x >= y + z:
	print("Not triangle")
	sys.exit(0)
else:
	print("Triangle")