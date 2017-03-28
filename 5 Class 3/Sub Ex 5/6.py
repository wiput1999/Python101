number = []
n = 0
cn = 0
p = 0
cp = 0


while True:
	i = int(input("Number : "))

	if i == 0:
		break
	elif i < 0:
		n+=i
		cn+=1
	else:
		p+=i
		cp+=1


rn = n/cn
rp = p/cp

print("Negative Avg :",rn)
print("Positive Avg :",rp)