A = int(input("A : "))
B = int(input("B : "))
C = int(input("C : "))
m = int(input("m : "))

if m > 5:
	Y = A*m*2 + B*m + C
elif m == 5:
	Y = A*m*2 + B*m - C
else:
	Y = A*m*2 + B*m
	
print(Y)