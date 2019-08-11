def factors(n):
	list = []
	for i in range(1,n+1):
		if n%i == 0:
			list.append(i)
	return(list)
call = factors(50)
print(call)