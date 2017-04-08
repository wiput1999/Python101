num = []


for i in range(10):
	num.append(int(input("Num : ")))

for j in range(0,len(num)):
	for i in range(0,len(num)-1-j):
		if num[i] > num[i+1]:
			t = num[i]
			num[i] = num[i+1]
			num[i+1] = t

print(num)