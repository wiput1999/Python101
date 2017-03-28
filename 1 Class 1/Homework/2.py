import numpy as np

a1 = float(input("a1 : "))
b1 = float(input("b1 : "))
c1 = float(input("c1 : "))
a2 = float(input("a2 : "))
b2 = float(input("b2 : "))
c2 = float(input("c2 : "))

eq_l = np.array([[a1,b1],[a2,b2]])
eq_r = np.array([[c1],[c2]])

result = np.linalg.solve(eq_l,eq_r)

print("x :", result[0][0])
print("y :", result[1][0])