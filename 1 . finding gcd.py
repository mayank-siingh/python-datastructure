def gcd(a,b,c):
	list = []
	list1 = []
	list2 = []
	list3 = []
	for i in range(1,a+1):
		if a%i == 0:
			list1.append(i) 
			i+=1
		else:
			i+=1
	for i in range(1,b+1):
		if b%i == 0:
			list2.append(i)
			i+=1
		else:
			i+=1
	for i in range(1,c+1):
		if c%i == 0:
			list3.append(i)
			i+=1
		else:
			i+=1
	for m in list1:
		if m in list2:
			if m in list3:
				list.append(m)
	print(max(list))
gcd(210,42,63)
			