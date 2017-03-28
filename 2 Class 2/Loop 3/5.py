import math

n = int(input("n : "))

i = 1
res = 0

while i <= n:
	res+=(1/i**2)
	i+=1

res = math.sqrt(6 * res)

print(res)