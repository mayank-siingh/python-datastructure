def isprime(n):
	list = []
	for i in range(2,n):
		if n%i == 0:
			list.append(i)
	if n == 1:
		return(False)
	elif list == []:
		return(True)
	else:
		return(False)
def mprime(m):
	count = 0
	i = 1
	list = []
	while count != m:
		if(isprime(i)):
			list.append(i)
			count += 1
		i += 1
	return(list)
call = mprime(10)
print(call)
