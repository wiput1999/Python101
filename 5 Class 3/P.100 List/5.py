number = []
count = 0

for i in range(10):
	number.append(int(input("Number : ")))

for i in range(10):
	if number[i] % 2 == 0:
		count+=1
	else:
		continue

print("Result :",count)