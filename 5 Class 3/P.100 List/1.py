number = []
even = False

for i in range(10):
	number.append(int(input("Number : ")))
	if number[i] % 2 == 0:
		even = True

if even == True:
	print("Have")
else:
	print("Not Have")