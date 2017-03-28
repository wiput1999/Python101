last_result = 0
result = 0

i = 1
while True:
	if i%4 == 1:
		result+=4*(1/i)
	elif i%4 == 3:
		result-=4*(1/i)
	if abs(result - last_result) < 0.0001:
		break
	last_result = result
	i+=2

print(result)