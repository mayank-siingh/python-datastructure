def divide(list):
	i = 0
	j = 0
	m = 1
	c = []
	pivot = list[0]
	while m < len(list):
		if pivot > list[m]:
			(list[m],list[i+1]) = (list[i+1],list[m])
			i+=1
			j+=1
		elif pivot < list[m]:
			j+=1
		m+=1
	(list[0],list[i]) = (list[i],list[0])
	a = sort(list[0:i])
	b = sort(list[i+1:len(list)])
	for n in range(0,len(a)):
		c.append(a[n])
	c.append(list[i])
	for n in range(0,len(b)):
		c.append(b[n])
		
	return(c)  

def sort(listt):
	
	for start in range(len(listt)):
		minpos = start
		for i in range(start,len(listt)):
			if listt[minpos] > listt[i]:
				minpos = i
		(listt[minpos],listt[start]) = (listt[start],listt[minpos])
	return(listt)
man = [10,9,1,34,56,23,21,6,11,7]
call = divide(man)
print(call)