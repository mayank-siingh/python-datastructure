def gcd(a,b,c):
	list = []
	for m in range(1,min(a+1,b+1,c+1)):
		if a%m == 0 and b%m == 0 and c%m == 0:
			list.append(m)
	print(max(list))
gcd(210,42,63)