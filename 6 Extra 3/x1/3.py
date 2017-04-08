x = int(input("x : "))
y = int(input("y : "))

while y != 0:
	r = x % y
	x = y
	y = r

print(x)