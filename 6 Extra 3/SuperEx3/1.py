a = []
count = 0

for i in range(10):
	a.append(int(input("Number : ")))

for x in a:
	if x >= 10:
		count+=1

print("Result :",count)