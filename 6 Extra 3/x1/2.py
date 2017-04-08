for num in range(100000000,1,-1):
	prime = True
	for i in range(2,num):
		if (num%i==0):
			prime = False
	if prime:
	   print(num)