income = [[],[],[],[],[],[],[]]
total = [0,0,0,0,0,0,0]

for i in range(7):
	for j in range(12):
		temp = int(input())
		income[i].append(temp)
		total[i]+=temp

print("======== Result by sector ========")
for i in range(7):
	for j in range(12):
		print("Department",i+1,"Sector",j+1,"got",income[i][j])
		
print("======== Result by department ========")
for i in range(7):
	print("Department",i+1,"got",total[i])

print("======== Overall Result ========")
print("Overall :",sum(total))