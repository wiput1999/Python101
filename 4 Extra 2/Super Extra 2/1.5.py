number = []
n = int(input("How many? : "))

for i in range(n):
	temp = int(input())
	number.append(temp)
	
total = sum(number)
avg = total / n
minimum = min(number)
maximum = max(number)

print("Max :",maximum)
print("Min ",minimum)
print("Avg :",avg)