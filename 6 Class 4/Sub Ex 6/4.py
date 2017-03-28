import sys

data = []
total = []

for i in range(2):
	data.append([])
	for j in range(3):
		data[i].append(int(input("Num : ")))

for i in range(2):
	temp = sum(data[i])
	total.append(temp)

print("Product       M1        M2         M3        TTL")
sys.stdout.write("A")
for x in data[0]:
	sys.stdout.write("           %s" % x)
sys.stdout.write("           %s" % total[0])
print()

sys.stdout.write("B")
for x in data[1]:
	sys.stdout.write("           %s" % x)
sys.stdout.write("           %s" % total[1])
print()

sys.stdout.write("Total")
for i in range(3):
	temp = data[0][i] + data[1][i]
	sys.stdout.write("         %s" % temp)
sys.stdout.write("         %s" % sum(total))