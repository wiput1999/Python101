def power(a,b):
	sum = 1
	for i in range(1,b+1):
		sum*=a
	return sum

x = power(2,10)

print(x)