result = 0

roman = str(input("Enter roman number : "))

n = len(roman)

for i in range(n):
	if roman[i] == "I":
		result+=1
	elif roman[i] == "V":
		result+=5
	elif roman[i] == "X":
		result+=10
	elif roman[i] == "L":
		result+=50
	elif roman[i] == "C":
		result+=100
	elif roman[i] == "D":
		result+=500
	elif roman[i] == "M":
		result+=1000
	else:
		pass
		
print(result)