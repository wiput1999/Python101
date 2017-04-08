def fac(b):
	sum = 1
	for i in range(1,b+1):
		sum*=i
	return sum

x = fac(5)

print(x)