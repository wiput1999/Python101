def power(a,b):
	sum = 1
	for i in range(0,b):
		sum*=a
	return sum

def fac(b):
	sum = 1
	for i in range(1,b+1):
		sum*=i
	return sum

def my_sin(x):
	sum = 0
	i = 1
	while i <= 17:
		if i % 4 == 1:
			sum+=((power(x,i))/fac(i))
		else:
			sum-=((power(x,i))/fac(i))
		i+=2
	return sum

x = my_sin(3.14159/2)

print(x)