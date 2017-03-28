numbers = []

n = int(input("n : "))

for a in range(0,n):
	new = float(input("Number:"))
	numbers.append(new)

avg = sum(numbers)/float(len(numbers))

print("======= Result =======")
print("Max :",max(numbers))
print("Avg :",avg)
print("Min :",min(numbers))