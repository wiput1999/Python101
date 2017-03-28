n = 0
p = 0


while True:
	i = int(input("Number : "))

	if i == 0:
		break
	elif i < 0:
		n+=i
	else:
		p+=i

print("Negative Total :",n)
print("Positive Total :",p)