cty_a = 50000000
cty_b = 70000000
count = 0

while cty_a < cty_b:
	cty_a*=1.03
	cty_b*=1.02
	count+=1
	
print(count)