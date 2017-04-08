i = 2
j = 3
ci = 1
cj = 0
cnt = 1
res = 4
while True:
	res*=(i/j)
	ci+=1
	cj+=1
	
	if ci == 2:
		ci = 0
		i+=2

	if cj == 2:
		cj = 0
		j+=2

	if abs(res - 3.141592) < 0.00000001:
		break

	cnt+=1
print(cnt)