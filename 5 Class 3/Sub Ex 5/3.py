choice = int(input("Choice [1-3] : "))

if choice == 1:
	n1 = float(input("n1 : "))
	n2 = float(input("n2 : "))
	r = n1 + n2
if choice == 2:
	n1 = float(input("n1 : "))
	n2 = float(input("n2 : "))
	r = n1 * n2
if choice == 3:
	n1 = float(input("n1 : "))
	n2 = float(input("n2 : "))
	r = n1 / n2
else:
	print("Only 1 - 3")

print(r)