a = []

for i in range(10):
	a.append(int(input("Number : ")))

V = int(input("V : "))

index = int(input("Index [0-9] : "))


a.pop()
a.insert(index,V)
print(a)