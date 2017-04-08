t = []
n = int(input("n : "))

for i in range(n):
	t.append(int(input("Input : ")))

s = []

for i in range(n//2):
	s.append(t[i] + t[n-1-i])

print(s)