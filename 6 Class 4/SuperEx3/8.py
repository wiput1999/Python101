x = [1,2,1,3,8,5,4,6,8,4,2,5,6,1,2,0,0,1,2]
y = [-1,0,1]
z = []

for i in range(0,len(x) - len(y)):
	k = 0
	for j in range(len(y)):
		k+=(x[i+j]*y[j])
	z.append(k)

print(x)
print(z)