import random

hour = []
total = []

for i in range(5):
    hour.append([])
    for j in range(7):
        hour[i].append(random.randrange(10))

for i in range(5):
    temp = 0
    for j in range(7):
        temp+=hour[i][j]
    total.append(temp)

for i in range(5):
    print("Employee",i+1,":",total[i])