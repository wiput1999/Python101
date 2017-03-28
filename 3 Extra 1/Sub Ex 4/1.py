numbers = []
total = 0
n = 100

for i in range(100):
	temp = int(input("Number :"))
	numbers.append(temp)
	total+=numbers[i]

avg = total/n
print()
print("======== Result =======")
print("Max :",max(numbers))
print("Avg :",avg)
print("Min :",min(numbers))