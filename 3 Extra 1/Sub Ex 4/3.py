a = []

for i in range(50):
	temp = int(input())
	a.append(temp)

print("======= Sum of 37 =======")
for i in range(50):
	for j in range(50):
		if a[i] + a[j] == 37:
			print(a[i],"and",a[j])
print("======= Maximum Even =======")
a.sort()

for i in range(49,0,-1):
	if a[i]%2 == 0:
		print(a[i])
		break
		
print("======= Count Odd Even =======")
odd = 0
even = 0

for i in range(50):
	if a[i]%2 == 0:
		even+=1
	else:
		odd+=1

print("Odd :",odd)
print("Even :",even)