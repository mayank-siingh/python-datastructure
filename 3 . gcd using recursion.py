def gcd(m,n):
	if m < n:
		(m,n) = (n,m)
	if m % n == 0:
		return(n)
	else:
		return(gcd(n,m%n))
call = gcd(38,95)#insert any random values to evaluate gcd
print(call)