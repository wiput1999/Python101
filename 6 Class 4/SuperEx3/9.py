import math

max_power = int(input("Max Power : "))
t = []

while True:
	k = int(input("T : "))
	if k == -999:
		break
	t.append(k)

s = []
power_count = max_power

for i in range(0,len(t)):
	if power_count != -1:
		s.append(t[i]/(power_count+1))
	else:
		s.append(t[i])
	power_count-=1

a = float(input("a : "))
b = float(input("b : "))

sum_a = 0
sum_b = 0
pc = max_power

for i in range(0,len(t)):
	if pc != -1:
		sum_a += s[i] * pow(a,pc+1)
		sum_b += s[i] * pow(b,pc+1)
	else:
		sum_a += s[i] * math.log(a)
		sum_b += s[i] * math.log(b)
	pc-=1

result = sum_b - sum_a
print(result)