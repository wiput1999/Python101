a = int(input("A :"))
b = int(input("B :"))
c = int(input("C :"))
d = int(input("D :"))
f = int(input("F :"))

total = a+b+c+d+f

result = (4*a + 3*b + 2*c + 1*d + 0*f)/total

print(result)
































'''
defs = (
	('A', 4),
	('B', 3),
	('C', 2),
	('D', 1),
	('F', 0)
)

sums = 0
weight_sums = 0

for letter, weight in defs:
	value = int(input(letter + ":"))
	
	sums += value
	weight_sums += value * weight
	
print("Result", weight_sums / sums)
'''