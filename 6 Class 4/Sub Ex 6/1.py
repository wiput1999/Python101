numbers = []

for i in range(10):
	numbers.append(int(input("Num : ")))

numbers.sort()

for x in numbers:
	if x % 2 == 1:
		min_odd = x
		break

for x in numbers:
	if x % 2 == 0:
		min_even = x
		break

for i in range(9,0,-1):
	if numbers[i] % 2 == 1:
		max_odd = numbers[i]
		break

for i in range(9,0,-1):
	if numbers[i] % 2 == 0:
		max_even = numbers[i]
		break

print()
print("Min odd : ",min_odd)
print("Min even : ",min_even)
print("Max odd : ",max_odd)
print("Max even : ",max_even)
