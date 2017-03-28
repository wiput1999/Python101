import statistics

number = []

for i in range(10):
	number.append(int(input("Number : ")))

result = statistics.mode(number)

print(result)