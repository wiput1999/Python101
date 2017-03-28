a = 1

while a <= 100:
	if a%3 == 0 and a%5 == 0:
		a+=1
		continue
	elif a%3 == 0:
		print(a)
	elif a%5 == 0:
		print(a)
	a+=1