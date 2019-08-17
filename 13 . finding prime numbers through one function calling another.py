#extract list of prime from numberlist
def prime(numberlist):
	l = []
	for x in numberlist:
		if prime_no(x):
			l.append(x)
	return(l)

def prime_no(n):
	y = True
	if n == 1:
		y = False
	for i in range(2,n):
		if n%i == 0:
			y =  False
	return(y)

list = [3,45,66,89,2,5,9,10,43,79]
call = prime(list)
print(call)
# 3,89,2,5,43,79