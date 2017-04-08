a = []

for i in range(10):
	a.append(int(input("Number : ")))

maxi = a[0]
max_index = 0

for i in range(10):
	if a[i] >= maxi:
		maxi = a[i]
		max_index = i

print("Max :",maxi)
print("At index",max_index)