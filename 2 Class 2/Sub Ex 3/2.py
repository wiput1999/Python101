hour = int(input("Hour : "))
minute = int(input("Minute : "))

free_hour = 1
hour_rate = 30

hour-=free_hour

if minute > 0:
	hour+=1

fee = hour*hour_rate

print("Fee :",fee)