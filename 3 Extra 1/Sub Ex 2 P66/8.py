total = 0
count = 0

while True:
	num = int(input("Num : "))
	total+=num
	count+=1
	con = str(input("Do you want to continue? (Y/N) : "))
	
	if con == "N":
		break

avg = total/count

print("Avg :",avg)
print("Total :",total)