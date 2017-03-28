number = []
count = 0

while True:
	temp = int(input())
	number.append(temp)
	if temp >= 100 and temp <= 200:
		count+=1
	elif temp == 0:
		break

print("Result :",count)