def factorial(n):
	if n <= 1:
		return(1)
	else:
		z = n * factorial(n-1)
		return(z)
call = factorial(6)#place any value to evaluate the factorial
print(call)