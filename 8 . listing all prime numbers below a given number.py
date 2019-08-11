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
def allprime(m):
	list = []
	for i in range(2,m):
		if(isprime(i)):
			list.append(i)
	return(list)
call = allprime(100)#number to be evaluated
print(call)
