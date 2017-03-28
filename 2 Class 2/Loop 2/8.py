import sys

a = 1
l = 1
c = 10

while a <= 10:
	b = 10
	d = 0
	while d <= c:
		sys.stdout.write(" ")
		d+=1
	if a%2 == 0:
		b = 1
		while b <= l:
			sys.stdout.write("%s" % b)
			b+=1
	else:
		b = l
		while b >= 1:
			sys.stdout.write("%s" % b)
			b-=1
	l+=2
	a+=1
	c-=1
	print()