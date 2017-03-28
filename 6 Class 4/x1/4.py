i = 1
res = 0
while True:
	if i % 4 == 1:
		res+=(1/i)
	else:
		res-=(1/i)
	if abs((res*4) - 3.141592) < 0.0000001:
		break
	i+=2

print(i)