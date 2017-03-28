n = ""
total = 0
count = 0

while True:
	n = int(input("n : "))
	if n < 0:
		print("ERROR NEGATIVE! ENTER POSITIVE!")
	elif n == 0:
		break
	else:
		total+=n
		count+=1

result = total/count

print(result)
		