import math

w = float(input("Weight :"))
h = float(input("Height :"))

M = math.sqrt((w*h)/3600)
D = 71.84*w**0.425*h**0.725/10000
B = 0.0003207*h**0.3*(1000*w)**(0.7285-0.0188**(3+math.log(10,w)))

print("Mosteller :",M)
print("Dubois :",D)
print("Boyd :",B)