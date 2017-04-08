import random
import time

num = []
random.seed()

for i in range(5000):
	num.append(int(random.randrange(10000)))

start = time.time()
num.sort()
end = time.time()

use = end - start

print("Complete using : ",use)