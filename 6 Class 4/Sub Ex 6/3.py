"""

Unsolved

"""
import numpy as np

a1 = []
a2 = []
s12 = []
a3 = []

""" a1 input """
for i in range(2):
	a1.append([])
	for j in range(2):
		a1[i].append(int(input("Num : ")))
		
""" a2 input """
for i in range(2):
	a2.append([])
	for j in range(2):
		a2[i].append(int(input("Num : ")))

for i in range(2):
	s12.append([])
	for j in range(2):
		s12[i].append(a1[i][j] + a2[i][j])

print(a1)
print(a2)
print(s12)
print(a3)