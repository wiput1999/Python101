d = []

G = float(input("G :"))
OD = float(input("OD :"))
sd = float(input("d :"))
n = float(input("n :"))
k = float(input("k :"))

d.append(sd)

i = 1
while 1:
	temp = ( ( 8 * k * n * ( OD - d[i-1] ) ** 3 ) / G ) ** (1/4)
	d.append(temp)
	if abs(d[i]-d[i-1]) < 0.000001:
		break
	i+=1

print()
print(d[i])
