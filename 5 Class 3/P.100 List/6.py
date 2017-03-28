number = []
result = 0

for i in range(10):
	number.append(int(input("Number : ")))

for i in range(10):
	result+=number[i]

print("Result :",result)