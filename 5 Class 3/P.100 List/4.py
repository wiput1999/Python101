number = []

for i in range(10):
	number.append(int(input("Number : ")))

print("===== Result =====")
for i in range(10):
	if number[i] % 2 == 0:
		print(number[i])
	else:
		continue