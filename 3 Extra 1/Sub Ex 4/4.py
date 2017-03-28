n = 2
h1 = []
h2 = []
h3 = []
h4 = []
h5 = []
mex = []
ex = []

for i in range(n):
	ih1 = float(input("h1:"))
	ih2 = float(input("h2:"))
	ih3 = float(input("h3:"))
	ih4 = float(input("h4:"))
	ih5 = float(input("h5:"))
	imex = float((input("Mid Ex:")))
	iex = float((input("Ex:")))
	h1.append(ih1)
	h2.append(ih2)
	h3.append(ih3)
	h4.append(ih4)
	h5.append(ih5)
	mex.append(imex)
	ex.append(iex)

print("======== Result ========")
for i in range(n):
	result = ((h1[i]+h2[i]+h3[i]+h4[i]+h5[i])/2.5) + mex[i]*3/10 + ex[i]/2
	print(i+1,":",result)