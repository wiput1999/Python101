a = 1
earning = 1

while earning >= 0:
	earning = int(input("Earning : "))
	if earning < 0:
		break
	elif earning < 10000:
		com = 0
	elif earning <= 25000:
		com = earning * 0.07
	else:
		com = earning * 0.1
	print("No","        ","Total Sales (Baht)","        ","Commission (Baht)")
	print(a,"            ",earning,"                    ",com)
	a+=1