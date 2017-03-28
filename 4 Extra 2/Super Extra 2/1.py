number = []

for i in range(10):
	temp = int(input())
	number.append(temp)
	
total = sum(number)
avg = total / 10
minimum = min(number)
maximum = max(number)

print("Max :",maximum)
print("Min ",minimum)
print("Avg :",avg)