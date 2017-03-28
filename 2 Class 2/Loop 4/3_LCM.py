a = int(input("a : "))
b = int(input("b : "))

i = a

while (a % i != 0 or b % i != 0):
	i-=1
	
hcf = i

lcm = a*b/hcf

print(lcm)