
palin_list = []
palin_str = []
palin = 0

data = str(input("String : "))
data = data.casefold()

rev_data = data[::-1]

temp = []

for i in range(len(data)):
	if rev_data[i] == data[i]:
		palin+=1
		temp.append(data[i])
	else:
		if palin!=0:
			palin_list.append(palin)
			palin_str.append(temp)
			temp = []
		palin = 0

if palin!=0:
	palin_list.append(palin)

if len(palin_list) != 0:
	print("Yes")
	print(palin_list)
	print(palin_str)
else:
	print("No")