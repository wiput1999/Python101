n = int(input("n : "))

rl = 0
lr = 0

for i in range(1,n+1):
	lr+=(1/i)
	
for i in range(n+1,1,-1):
	rl+=(1/i)

print("Left to Right :",lr)
print("Right to Left :",rl)
print("Diff :",abs(lr-rl))