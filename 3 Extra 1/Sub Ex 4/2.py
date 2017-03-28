a = []
b = []

for i in range(50):
	temp = int(input("a :"))
	a.append(temp)
	
i = 1
while i <= 50:
	b.append(a[i])
	b.append(a[i-1])
	i+=2
	
print()
print(b)