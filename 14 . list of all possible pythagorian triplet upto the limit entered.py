n = int(input("Enter the number upto which you want all possible pair of pythagorian triplet"))
def pythagorus(x):
	list = []
	for i in range(1,x):
		for j in range(1,x):
			for k in range(1,x):
				if k**2 + j**2 == i**2:
					list.append([k,j,i])
	print(len(list))
	return(list)
call = pythagorus(n)
print(call)
