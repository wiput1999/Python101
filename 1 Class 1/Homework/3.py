import math

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

result_p = (-b + math.sqrt(b**2 - 4*a*c))/2*a
result_s = (-b - math.sqrt(b**2 - 4*a*c))/2*a

print("Result 1 :",result_p)
print("Result 2 :",result_s)