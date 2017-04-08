str1 = str(input("str1 : "))
str2 = str(input("str2 : "))
num = int(input("number : "))

if num > len(str1):
	print(str1+str2)
else:
	result = str1[:num] + str2 + str1[num:]
	print(result)