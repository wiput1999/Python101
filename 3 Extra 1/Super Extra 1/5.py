import math
import sys

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

if a >= b and a >= c:
	x = a
	y = b
	z = c
elif b >= a and b >= c:
	x = b
	y = a
	z = c
else:
	x = c
	y = b
	z = a

if x >= y + z:
	print("Not triangle")
	sys.exit(0)
else:
	if x == y == z:
		print("ด้านเท่า")
	elif x == y or x == z or y == z:
		print("หน้าจั่ว")
	elif y**2 + z**2 > x**2:
		print("มุมแหลม")
	elif y**2 + z**2 < x**2:
		print("มุมป้าน")
	elif x == math.sqrt(y**2 + z**2):
		print("มุมฉาก")
	else:
		print("ธรรมดา")