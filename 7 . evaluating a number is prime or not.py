def prime(n):
	list = []
	for i in range(2,n):
		if n%i == 0:
			list.append(i)
	if list == []:
		print("no. is prime")
	else:
		print("no. is not a prime")
prime(121) # enter value for evaluation