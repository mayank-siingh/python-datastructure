def factorial(n):
	i = 1
	for j in range(2,n+1):
		i = i * j
	return(i)
call = factorial(6)
print(call)