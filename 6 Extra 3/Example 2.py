import random
import time

num = []
random.seed()

for i in range(5000):
	num.append(int(random.randrange(10000)))

start = time.time()
# Own Bubble Sort
for j in range(0,len(num)):
	for i in range(0,len(num)-1-j):
		if num[i] > num[i+1]:
			t = num[i]
			num[i] = num[i+1]
			num[i+1] = t
end = time.time()

use = end - start
	
print("Complete using : ",use)