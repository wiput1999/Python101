total = 0
count = 0
num = ""

while True:
	num = int(input("Num : "))
	if num == 0:
		break
	total+=num
	count+=1

avg = total/count

print("Avg :",avg)
print("Sum :",total)