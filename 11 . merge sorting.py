def merge(A,B):
	(C,m,n) = ([],len(A),len(B))
	(i,j) = (0,0)
	while i+j < m+n:
		if i == m:
			C.append(B[j])
			j+=1
		elif j == n:
			C.append(A[i])
			i+=1
		elif A[i] < B[j]:
			C.append(A[i])
			i+=1
		elif A[i] > B[j]:
			C.append(B[j])
			j+=1
	return(C)
def merge_sort(list,left,right):
	if right - left <= 1:
		return(list[left:right])
	if right -left > 1:
		mid = (left+right) // 2
		l = merge_sort(list,left,mid)
		r = merge_sort(list,mid,right)
		return(merge(l,r))
		
liist = [10,34,-78,41,3,-10,5,339,55,32,95,1]
call = merge_sort(liist,0,len(liist))

print(call)
