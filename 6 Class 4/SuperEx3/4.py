a = []
index = -1

for i in range(10):
	a.append(int(input("Number : ")))

V = int(input("V : "))

for i in range(10):
	if a[i] == V:
		index = i

if index == -1:
	print("Not found")
else:
	a.pop(index)
	a.append(0)
	print(a)