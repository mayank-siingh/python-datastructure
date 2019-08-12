def sort(list):
	
	for start in range(len(list)):
		minpos = start
		for i in range(start,len(list)):
			if list[minpos] > list[i]:
				minpos = i
		(list[minpos],list[start]) = (list[start],list[minpos])
	return(list)
list1 = [1,2,3,4,34,45,12,23,90,67]
call = sort(list1)
print(call)