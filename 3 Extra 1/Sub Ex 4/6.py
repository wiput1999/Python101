income = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
total = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(3):
	for j in range(5):
		for k in range(5):
			temp = int(input())
			income[i][j].append(temp)
			total[i][j]+=temp

print("======== Outcome by department on Tue ========")
for i in range(3):
	print("Department",i+1,"have outcome",total[i][j])
		
print("======== Result in sector 4 ========")
result = 0
for i in range(3):
	for j in range(5):
		result+=income[i][3][j]
print("Sector 4 have outcome",result)

print("======== Highest outcome department ========")
dp1 = sum(total[0])
dp2 = sum(total[1])
dp3 = sum(total[2])

if dp1 > dp2 and dp1 > dp3:
	print("Department 1 have hightest outcome")
elif dp2 > dp1 and dp2 > dp3:
	print("Department 2 have hightest outcome")
elif dp3 > dp2 and dp3 > dp1:
	print("Department 3 have hightest outcome")