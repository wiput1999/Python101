a = []

for i in range(10):
	a.append(int(input("Number : ")))

have = False

V = int(input("V : "))

for x in a:
	if x == V:
		have = True
		break

print(V,"is" if have else "is not","in list")