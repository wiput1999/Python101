#Page 32 #1

w = float(input("Weight : "))
h = float(input("Height (cm) : ")) / 100 #Convert cm to m

BMI = w/(h**2)

if BMI < 20:
	print("Thin")
elif BMI < 25:
	print("Normal")
else:
	print("Fat")