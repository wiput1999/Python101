palin_list = []
palin = 0

data = str(input("String : "))
data = data.casefold()

rev_data = data[::-1]

for i in range(len(data)):
	if rev_data[i] == data[i]:
		palin+=1
	else:
		if palin!=0:
			palin_list.append(palin)
		palin = 0

if palin!=0:
	palin_list.append(palin)

if len(palin_list) != 0:
	print("Yes")
	print(palin_list)
else:
	print("No")