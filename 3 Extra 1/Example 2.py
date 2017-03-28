total = 0
n = ""
while n != 0:
	n = int(input("n :"))
	if n%2 == 1:
		total += n
	
print(total)